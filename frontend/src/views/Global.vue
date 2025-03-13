<template>
    <v-container>
        <v-row justify="center">
            <v-col cols="12" sm="6">
                <v-card color="purple">
                        <v-card-title class="headline" align="center" >*** REAL-TIME WEATHER ***</v-card-title>
                            <v-card-text>
                                <v-text-field v-model="cityName" label="Enter a location"></v-text-field>
                                <v-btn @click= getWeather(); color="yellow">Get Weather</v-btn>
                                <v-divider></v-divider>
                                <v-alert v-if="error" type="error">{{ error }}</v-alert>
                            </v-card-text>
                        </v-card>
                    </v-col>
                </v-row>
                <v-row justify="center">
                    <p>Location: <span class="text-blue" id="City"></span><br> Temperature: <span class="text-red" id="Temp"></span> °C<br> Min Temp: <span class="text-blue" id="Min Temp"></span> °C<br> Max Temp: <span class="text-red" id="Max Temp"></span> °C<br> Heat Index: <span class="text-blue" id="Heat Index"></span> °C<br> Humidity: <span class="text-red" id="Humidity"></span> %<br> Pressure: <span class="text-blue" id="Pressure"></span> hPa</p>
                </v-row>
    </v-container>
</template>

<script setup>
/** JAVASCRIPT HERE */

// IMPORTS
import { ref,reactive,watch ,onMounted,onBeforeUnmount,computed } from "vue";  
import { useRoute ,useRouter } from "vue-router";
import { useMqttStore } from "@/store/mqttStore";
import { useAppStore } from "@/store/appStore";
import { storeToRefs } from "pinia";
// Highcharts, Load the exporting module and Initialize exporting module.
import Highcharts from 'highcharts';
import more from 'highcharts/highcharts-more';
import Exporting from 'highcharts/modules/exporting';
Exporting(Highcharts); 
more(Highcharts);

// VARIABLES
const Mqtt = useMqttStore();
const { payload, payloadTopic } = storeToRefs(Mqtt);
// VARIABLES
const router      = useRouter();
const route       = useRoute();  
// const led = reactive({"brightness":255,"nodes":1,"color":{ r: 255, g: 0, b: 255, a: 1 }});
let timer, ID = 1000;
const points = ref(10); // Specify the quantity of points to be shown on the live graph simultaneously.
const shift = ref(false); // Delete a point from the left side and append a new point to the right side of the graph.
const apiKey = "ec93b156a9d6f88b5c58b38d2c0d783f";
//var cityId = "";
const cityName = ref('');
const error = ref('');
//const payload           = ref({"Type":"Sensor", "ID":620157646, "DHT_Temperature":0, "BMP_Temperature":0, "DHT_Humidity":0, "DHT_HeatIndex":0, "BMP_Pressure":0, "BMP_Altitude":0, "Soil_Moisture":0});
// OpenWeatherMap API Key: ec93b156a9d6f88b5c58b38d2c0d783f

// FUNCTIONS
onMounted(()=>{
    // THIS FUNCTION IS CALLED AFTER THIS COMPONENT HAS BEEN MOUNTED 
    Mqtt.connect(); // Connect to Broker located on the backend
    setTimeout( ()=>{
        // Subscribe to each topic
        Mqtt.subscribe("620157646"); 
        Mqtt.subscribe("620157646_pub");
    },3000);
});

onBeforeUnmount(()=>{
    // THIS FUNCTION IS CALLED RIGHT BEFORE THIS COMPONENT IS UNMOUNTED
    Mqtt.unsubcribeAll();
});

// https://api.openweathermap.org/data/2.5/find?q=Kingston&appid=ec93b156a9d6f88b5c58b38d2c0d783f
const getWeather = async () => {
  try {
    const response = await fetch(`http://api.openweathermap.org/data/2.5/weather?q=${cityName.value}&units=metric&appid=${apiKey}`);
    const data = await response.json();
    document.getElementById("City").textContent = data.name;
    document.getElementById("Temp").textContent = data.main.temp;
    document.getElementById("Min Temp").textContent = data.main.temp_min;
    document.getElementById("Max Temp").textContent = data.main.temp_max;
    document.getElementById("Heat Index").textContent = data.main.feels_like;
    document.getElementById("Humidity").textContent = data.main.humidity;
    document.getElementById("Pressure").textContent = data.main.pressure;
  } catch (error) {
    console.error(error);
    error.value = 'Failed to fetch weather data';
  }
};

</script>

<style scoped>
/** CSS STYLE HERE */

</style>