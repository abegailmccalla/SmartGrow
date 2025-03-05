<template>
    <v-container>
        <v-sheet class="bg-surface mb-6" align="center">
            <v-row class="pb-2 mb-2" color="surface" rounded="xl" align="center">
                <v-col align="start">
                    <v-sheet class="rounded-t-lg mb-1 pa-5" elevation="0" max-width="800" width="100%">
                        <v-card class="text-secondary" title="Artificial Sunlight Controls" color="surface" subtitle="with preset modes" elevation="0">
                            <v-slider class="pt-2 bg-surface" append-icon="mdi:mdi-car-light-high" density="compact" thumb-size="16" color="secondary" label="Brightness" direction="horizontal" min="0" max="250" step="10" show-ticks thumb-label="always" v-model="led.brightness"></v-slider>
                            <v-row class="d-flex justify-space-between px-4 pa-4">
                                <v-col>
                                    <v-btn rounded="xl" size="x-large" color="red" class="text-white" @click="LightPreference(1)">Growth</v-btn>
                                </v-col>
                                <v-col>
                                    <v-btn rounded="xl" size="x-large" color="orange" class="text-white" @click="LightPreference(2)">Bloom</v-btn>
                                </v-col>
                                <v-col>
                                    <v-btn rounded="xl" size="x-large" color="green" class="text-white" @click="LightPreference(3)">Veg</v-btn>
                                </v-col>
                                <v-col>
                                    <v-btn rounded="xl" size="x-large" color="grey" class="text-white" @click="LightPreference(4)">Off</v-btn>
                                </v-col>
                            </v-row>
                        </v-card>
                    </v-sheet>
                </v-col>
                <v-col align="center">
                    <v-color-picker v-model="led.color"></v-color-picker>
                    
                </v-col>
            </v-row><br>
            <v-row class="rounded-t-lg mb-1 pa-5" align="center" justify="center">
                <v-col cols="12" align="center">
                    <v-card class="text-secondary" title="Crop Selection" color="surface" elevation="0">
                        <v-select class="text-secondary" dense v-model="crops.name" :items="['Tomato', 'Cucumber', 'Pepper', 'Lettuce', 'Spinach', 'Kale', 'Basil', 'Cilantro', 'Parsley', 'Chives']" label="Select Crop" item-text="name" item-value="name" color="secondary" prepend-icon="mdi:mdi-sprout"></v-select>
                    </v-card>
                    <v-btn class="text-white" color="primary" :disabled="!crops.name" @click="updateCrop(crops)">Update Crop</v-btn>
                </v-col>
            </v-row>

        </v-sheet>
    </v-container>
</template>

<script setup>
/** JAVASCRIPT HERE */

// IMPORTS
// Highcharts, Load the exporting module and Initialize exporting module.
import Highcharts from 'highcharts';
import more from 'highcharts/highcharts-more';
import Exporting from 'highcharts/modules/exporting';
Exporting(Highcharts);
more(Highcharts);


import { useMqttStore } from '@/store/mqttStore'; // Import Mqtt Store
// import WeatherWidget from '@/components/WeatherWidget.vue'
import { storeToRefs } from "pinia";
import { useAppStore } from "@/store/appStore";
import { ref,reactive,watch ,onMounted,onBeforeUnmount,computed } from "vue";  
import { useRoute ,useRouter } from "vue-router";

// VARIABLES
const router      = useRouter();
const route       = useRoute();  
const Mqtt = useMqttStore();
const AppStore = useAppStore();
const { payload, payloadTopic } = storeToRefs(Mqtt);
const mqtt = ref(null);
const host = ref("dbs.msjrealtms.com"); // Host Name or IP address
const port = ref(9002); // Port number
const points = ref(10); 
const selected = ref([]); // Selected units
const led = reactive({"brightness":255,"nodes":1,"color":{ r: 45, g: 120, b: 150, a: 1 }});
let timer, ID = 1000;
const colourPreset = reactive({
    "growth": { r: 255, g: 0, b: 0, a: 1 },
    "bloom": { r: 255, g: 200, b: 0, a: 1 },
    "veg": { r: 0, g: 200, b: 0, a: 1 },
    "off": { r: 0, g: 0, b: 0, a: 1 }

});

const crops = reactive({name: null});

// FUNCTIONS

const LightPreference = (mode) => {
    if(mode === 1){
        led.color = colourPreset.growth;
    }else if(mode === 2){
        led.color = colourPreset.bloom;
    }else if(mode === 3){
        led.color = colourPreset.veg;
    }else{
        led.color = colourPreset.off;
    }
    
};

// FUNCTIONS
onMounted(()=>{
    // THIS FUNCTION IS CALLED AFTER THIS COMPONENT HAS BEEN MOUNTED
  
    Mqtt.connect(); // Connect to Broker located on the backend
    setTimeout( ()=>{
    // Subscribe to each topic
    Mqtt.subscribe("620154701");
    Mqtt.subscribe("620154701_pub");}, 3000);
});


onBeforeUnmount(()=>{
    // THIS FUNCTION IS CALLED RIGHT BEFORE THIS COMPONENT IS UNMOUNTED
    Mqtt.unsubcribeAll();
});

const updateCrop = async (crops) => {
    const data = await AppStore.updateCropData(crops.name);
    console.log(crops.name);
    console.log(data);
};



watch(led,(controls)=>{
    clearTimeout(ID);

    ID = setTimeout(()=>{
        const message =
JSON.stringify({"type":"controls","brightness":controls.brightness,"leds":controls.nodes,"color": controls.color});
        Mqtt.publish("620154701_sub",message); // Publish to a topic subscribed to by the hardware
    },1000)
});


</script>

<style scoped>
/** CSS HERE */
</style>
```
