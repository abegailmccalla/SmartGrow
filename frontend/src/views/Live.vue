<template>
    <v-container class="bg-surface mb-6" align="center">
        <v-sheet class="pb-2 mb-2" color="surface" rounded="xl" align="center">
           
            <v-row :max-width="1000">
                <v-col class="d-flex justify-center">
                    <v-sheet class="d-inline justify-center">
                        <v-row>
                           
                                

                            <v-col cols="4" >
                                
                                <v-card :width="360" :height="400" class="text-secondary" color="surface">
                                    <v-card-title>
                                        <v-icon left>mdi-cloud</v-icon>
                                        Inside Environment
                                    </v-card-title>
                                    <v-card-text>
                                        <v-row class="d-flex justify-space-between px-4 pa-2">
                                            <v-card-subtitle class="">MAX</v-card-subtitle>
                                            <v-card-subtitle class="">MIN</v-card-subtitle>
                                        </v-row>                                            <!-- <v-card-text>Temperature</v-card-text> -->
                                        <v-row class="d-flex justify-space-between">
                                            <v-card-text>Temperature</v-card-text>
                                            <!-- <span class="label">Temperature</span>
                                            <span class="text-h6">{{ temperature }}</span> -->
                                            <!-- <span class="text-red">{{ tempDiff }}</span> -->
                                        </v-row>
                                        <v-row class="d-flex align-center justify-space-between">
                                            <v-card-text class="text-red">{{ cropSelected.highTemp }} °C</v-card-text>
                                            <v-card-text class="text-h6">{{ temperature }}</v-card-text>
                                            <v-card-text class="text-red">{{ cropSelected.lowTemp }} °C</v-card-text>
                                        </v-row>

                                        <v-row class="d-flex justify-space-between">
                                            <v-card-text>Humidity</v-card-text>

                                            <!-- <span class="label">Temperature</span>
                                            <span class="text-h6">{{ temperature }}</span> -->
                                            <!-- <span class="text-red">{{ tempDiff }}</span> -->
                                        </v-row>
                                        <v-row class="d-flex align-center justify-space-between">
                                            <v-card-text class="text-red">{{ cropSelected.highHumidity}} %</v-card-text>
                                            <v-card-text class="text-h6">{{ humidity }}</v-card-text>
                                            <v-card-text class="text-red">{{ cropSelected.lowHumidity}} %</v-card-text>
                                        </v-row>
                                        <v-row class="d-flex justify-space-between">
                                            <v-card-text>Heat Index</v-card-text>
                                            <!-- <span class="label">Temperature</span>
                                            <span class="text-h6">{{ temperature }}</span> -->
                                            <!-- <span class="text-red">{{ tempDiff }}</span> -->
                                        </v-row>
                                        <v-row class="d-flex align-center justify-space-between">
                                            <v-card-text class="text-red">{{ cropSelected.maxheatindex}} °C</v-card-text>
                                            <v-card-text class="text-h6">{{ heatindex }}</v-card-text>
                                            <v-card-text class="text-red">{{ cropSelected.minheatindex }} °C</v-card-text>
                                        </v-row>
                                       
                                    </v-card-text>
                                        
                                </v-card>
                           
                            </v-col>
                        </v-row>
                    </v-sheet>
                </v-col>
                <v-col cols="4">
                    <v-row>
                        <v-col>
                                <v-card :width="350" :height="70" class="text-secondary" color="onPrimary" elevation="0">
                                    <v-card-title>{{ cropSelected.name }}</v-card-title>
                                    <v-card-subtitle>being cultivated</v-card-subtitle>    
                                </v-card>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col class="d-flex justify-end" cols="6">
                            <v-card elevation="0">
                                <v-slider class="slider" readonly thumb-label color="blue" v-model="waterSlider" direction="vertical" label="Water Reservoir" track-size="50">
                                </v-slider>
                            </v-card>
                        </v-col>
                        <v-col class="d-flex justify-start" cols="6">
                            <v-card elevation="0">
                                <v-slider class="slider" readonly thumb-label color="tertiary" v-model="fertilizerSlider" direction="vertical" label="Fertilizer Tray" track-size="50">
                                </v-slider>
                            </v-card>
                        </v-col>
                    </v-row>
                </v-col>
                <v-col cols="4">
                    <figure class="highcharts-figure">
                        <div id="container6"></div>
                    </figure>
                </v-col>
            </v-row>
           
           
            <v-row>
                <v-col cols="12">
                    <figure class="highcharts-figure">
                        <div id="container"></div>
                    </figure>
                </v-col>
            </v-row>
            <v-row justify="start">
                <v-col cols="12">
                    <figure class="highcharts-figure">
                        <div id="container1"></div>
                    </figure>
                </v-col>
            </v-row>
        </v-sheet>
        
    </v-container>
    <v-sheet class="mb-2" color="surface" align="center" style="position:fixed; top: 59%; right: 30px; transform: translateY(-50%); z-index: 1000;">
        <v-row class="d-flex justify-center">
            <v-col cols="12" class="d-flex justify-center">
                <v-card :width="120" :height="600" class="text-secondary" color="surface">
                    <v-card-text>
                        Actuator Status
                        </v-card-text>
                    <v-card-text>
                        <v-row class="d-flex justify-center align-center px-4 pa-5">
                           <v-card-subtitle class="m-6 p-6">Fan</v-card-subtitle>
                           <v-icon size="70" color="primary" class="mdi-spin">mdi-fan</v-icon>
                           <span class="status">{{ fanStatus.value ? 'Active' : 'Inactive' }}</span>
                        </v-row>
                        <v-row class="d-flex justify-center align-center px-4 pa-9">
                           <v-card-subtitle class="m-6 p-6">Heater</v-card-subtitle>
                           <v-icon size="70" color="primary">mdi-heat-wave</v-icon>
                           <span class="status">{{ heaterStatus.value ? 'Active' : 'Inactive' }}</span>
                        </v-row>
                        <v-row class="d-flex justify-center align-center px-4 pa-9">
                           <v-card-subtitle class="m-6 p-6">Irrigation</v-card-subtitle>
                           <v-icon size="70" color="primary">mdi-watering-can</v-icon>
                           <span class="status">{{ pumpStatus.value ? 'Active' : 'Inactive' }}</span>
                        </v-row>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-sheet>
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
import { ref,reactive,watch ,onMounted,onBeforeUnmount,computed } from "vue";  
import { useRoute ,useRouter } from "vue-router";
import { useAppStore } from "@/store/appStore";
import App from '@/App.vue';
 
 
// VARIABLES
const router      = useRouter();
const route       = useRoute();  
const AppStore = useAppStore();
const Mqtt = useMqttStore();
const { payload, payloadTopic } = storeToRefs(Mqtt);
const mqtt = ref(null);
const host = ref("dbs.msjrealtms.com"); // Host Name or IP address
const port = ref(9002); // Port number
const points = ref(10); // Specify the quantity of points to be shown on the live graph simultaneously.
const shift = ref(false); // Delete a point from the left side and append a new point to the right side of the graph.
const isUmbrella = ref("02"); // Weather icon
const tempunits = ref("Fahrenheit"); // Temperature units
const tempChart = ref(null); // Chart object
const HiChart = ref(null); // Chart object
const altChart = ref(null); // Chart object
const soilChart = ref(null); // Chart object
const heightChart = ref(null); // Chart object 
let isCelsius = true; // Temperature units
const hasSaved = false // Save status

let moist = ref(10); // soil moisture
let soilMoist = 200; // soil moisture
let tankLevel = ref(10); // tank level
const selected = ref([]); // Selected units
const actuateMsg = ref({"type":"actuate","fan":false, "pump":false, "heater":false});
let pumpStatus = reactive({value:false}); // Pump status
let pumpStatusAlert = {alertedWater:false, alertedFertilizer:false}; // Pump status alert
let heaterStatus = reactive({value:false}); // Heater status
let fanStatus = reactive({value:false}); // Fan status


const led = reactive({"brightness":255,"nodes":1,"color":{ r: 45, g: 120, b: 150, a: 1 }});
let timer, ID = 1000;
const indicatorColor = computed(()=>{
    return `rgba(${led.color.r},${led.color.g},${led.color.b},${led.color.a})`
});


const fertilizerSlider = ref(50);
const waterSlider = ref(50);
let tempDiff = reactive({value:0});
let humDiff = reactive({value:0});
let heatDiff = reactive({value:0});



const temperature = computed(()=>{
    if(!!payload.value){
        if(isCelsius){
            tempDiff = Math.abs(payload.value.temperature - cropSelected.temperature).toFixed(2);
            return `${payload.value.temperature.toFixed(2)} °C`;
        }else{
            return `${convertToFahrenheit(payload.value.temperature).toFixed(2)} °F`;
        }
    }
});


function calculateHeatIndex(tempC, RH) {
  // Step 1: Convert Celsius to Fahrenheit
  const T = tempC * 9 / 5 + 32;

  // Step 2: Calculate heat index in Fahrenheit using Rothfusz formula
  let HI = -42.379 +
           2.04901523 * T +
           10.14333127 * RH -
           0.22475541 * T * RH -
           0.00683783 * T * T -
           0.05481717 * RH * RH +
           0.00122874 * T * T * RH +
           0.00085282 * T * RH * RH -
           0.00000199 * T * T * RH * RH;

  // Low humidity adjustment
  if (RH < 13 && T >= 80 && T <= 112) {
    const adjustment = ((13 - RH) / 4) * Math.sqrt((17 - Math.abs(T - 95)) / 17);
    HI -= adjustment;
  }

  // High humidity adjustment
  else if (RH > 85 && T >= 80 && T <= 87) {
    const adjustment = ((RH - 85) / 10) * ((87 - T) / 5);
    HI += adjustment;
  }

  // Step 3: Convert back to Celsius
  const HI_C = (HI - 32) * 5 / 9;

  return HI_C;
}


const heatindex = computed(()=>{
    if(!!payload.value){
        return `${calculateHeatIndex(payload.value.temperature, payload.value.humidity).toFixed(2)} °C`;
    }


});
const humidity = computed(()=>{
    if(!!payload.value){
    humDiff = Math.abs(payload.value.humidity - cropSelected.humidity).toFixed(2);
    return `${payload.value.humidity.toFixed(2)} %`;
    }
});



const CreateCharts = async () => {
// TEMPERATURE CHART
    tempChart.value = Highcharts.chart('container', {
    chart: { zoomType: 'x' },
    title: { text: 'Temperature and Heat Index Analysis (Live)', align: 'left' },
    yAxis: {
    title: { text: '°C', style:{color:'#000000'}},
    labels: { format:'{value} °C' }
    },
    xAxis: {
    type: 'datetime',
    title: { text: 'Time', style:{color:'#000000'} },
    },
    tooltip: { shared:true, },
    series: [
    {
    name: 'Temperature',
    type: 'spline',
    data: [],
    turboThreshold: 0,
    color: Highcharts.getOptions().colors[8]
    },
    {
    name: 'Heat Index',
    type: 'spline',
    data: [],
    turboThreshold: 0,
    color: Highcharts.getOptions().colors[6]
    } ],
    });
    
    HiChart.value = Highcharts.chart('container1', {
    chart: { zoomType: 'x' },
    title: { text: 'Humidity Analysis (Live)', align: 'left' },
    yAxis: {
    title: { text: '%' , style:{color:'#000000'}},
    labels: { format: '{value} %' }
    },
    xAxis: {
    type: 'datetime',
    title: { text: '', style:{color:'#000000'} },
    },
    tooltip: { shared:true, },
    series: [
    {
    name: 'Humidity',
    type: 'spline',
    data: [],
    turboThreshold: 0,
    color: Highcharts.getOptions().colors[14]
    } ],
    });

    

        soilChart.value = Highcharts.chart('container6', {
        title: { text: 'Soil Moisture (Live)', align: 'left' },// the value axis
        yAxis: {
        min: 0,
        max: 100,
        tickPixelInterval: 72,
        tickPosition: 'inside',
        tickColor: Highcharts.defaultOptions.chart.backgroundColor || '#FFFFFF',
        tickLength: 20,
        tickWidth: 2,
        minorTickInterval: null,
        labels: { distance: 20, style: { fontSize: '14px' } },
        lineWidth: 0,
        plotBands: [{ from: 0, to: 20, color: '#DF5353', thickness: 20 }, { from: 20, to: 60, color: '#DDDF0D', thickness: 20
        }, { from: 60, to: 100, color: '#55BF3B', thickness: 20 }]
        },
        tooltip: { shared:true, },
        pane: { startAngle: -90, endAngle: 89.9, background: null, center: ['50%', '75%'], size: '110%' },
        series: [{
        type:'gauge',
        name: 'Soil Moisture',
        data:[0],
        tooltip: { valueSuffix: ' %' },
        dataLabels: { format: '{y} %', borderWidth: 0, color: ( Highcharts.defaultOptions.title &&
        Highcharts.defaultOptions.title.style && Highcharts.defaultOptions.title.style.color ) || '#333333', style: { fontSize: '16px' }
        },
        dial: { radius: '80%', backgroundColor: 'gray', baseWidth: 12, baseLength: '0%', rearLength: '0%' },
        pivot: { backgroundColor: 'gray', radius: 6 }
        }]
        });
                    

};

const cropSelected = reactive({ name: 'Carrot' });
const CropData = async () => {
    // Code to read passcode here
    
    const data= await AppStore.getCropData();
    console.log(data);
    cropSelected.name = data[0].name.charAt(0).toUpperCase() + data[0].name.slice(1);
    // cropSelected.lowTemp = data[0].lowest_temperature.toFixed(2);
    cropSelected.lowTemp = data[0]['Min temperature'].toFixed(2);
    // cropSelected.highTemp = data[0].highest_temperature.toFixed(2);
    cropSelected.highTemp = data[0]['Max temperature'].toFixed(2);
    // cropSelected.lowSoilMoisture = data[0].lowest_soil_moisture.toFixed(2);
    // cropSelected.highSoilMoisture = data[0].highest_soil_moisture.toFixed(2);
    cropSelected.lowSoilMoisture = data[0]['Min soil moisture'].toFixed(2);
    cropSelected.highSoilMoisture = data[0]['Max soil moisture'].toFixed(2);

    // cropSelected.lowHumidity = data[0].lowest_humidity.toFixed(2);
    cropSelected.highHumidity = data[0]['Max humidity'].toFixed(2);
    cropSelected.lowHumidity = data[0]['Min humidity'].toFixed(2);
    // cropSelected.highHumidity = data[0].highest_humidity.toFixed(2);
    // cropSelected.lowHeatIndex = data[0].lowest_heat_index.toFixed(2);
    // cropSelected.highHeatIndex = data[0].highest_heat_index.toFixed(2);

    cropSelected.maxheatindex = calculateHeatIndex(cropSelected.highTemp, cropSelected.highHumidity).toFixed(2);
   
    cropSelected.minheatindex = calculateHeatIndex(cropSelected.lowTemp, cropSelected.lowHumidity).toFixed(2);

    console.log(cropSelected);

    

    
    console.log(data);
    console.log(cropSelected.name);
    
};
CropData();



// FUNCTIONS
onMounted(()=>{
    // THIS FUNCTION IS CALLED AFTER THIS COMPONENT HAS BEEN MOUNTED
    CreateCharts();

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




watch(payload,(data)=> {
        if(points.value > 0){ points.value -- ; }
        else{ shift.value = true; }

        
    soilChart.value.series[0].points[0].update(data.soilmoisture);

    waterSlider.value = 26;
    fertilizerSlider.value = 72;

    soilMoist = data.soilmoisture + 150;

    if (data.temperature > cropSelected.highTemp) {
        fanStatus.value = true;
        heaterStatus.value = false;
    } else if (data.temperature < cropSelected.lowTemp) {
        fanStatus.value = false;
        heaterStatus.value = true;
        
    } else {
        fanStatus.value = false;
        heaterStatus.value = false;
        
    }

    if (data.soilmoisture < ((cropSelected.lowSoilMoisture / cropSelected.highSoilMoisture) * 100)) { 
        pumpStatus.value = true;
    } else {
         pumpStatus.value = false;
    }
    console.log("Soil Moisture: ", data.soilmoisture);
    console.log("Water Level: ", data.water);
    
    if(data.water< 20){
        alert("Water level is critically low");
        pumpStatusAlert.alertedWater = true;
        pumpStatus.value = false;
        console.log(pumpStatusAlert.alertedWater);
    }

    if(data.fertilizer< 20){
        alert("Fertilizer level is critically low");
        pumpStatusAlert.alertedFertilizer = true;
        pumpStatus.value = false;
        console.log(pumpStatusAlert.alertedFertilizer);
    }

const newActuateMsg = { "type": "actuate", "fan": fanStatus.value, "pump": pumpStatus.value, "heater": heaterStatus.value };
if (JSON.stringify(actuateMsg.value) !== JSON.stringify(newActuateMsg)) {
    actuateMsg.value = newActuateMsg;
    Mqtt.publish("620154701_sub", JSON.stringify(actuateMsg.value)); // Publish to a topic subscribed to by the hardware
    console.log("Actuate Message: ", actuateMsg.value);
    pumpStatus = false;
}

    
   if(isCelsius){

        tempChart.value.series[0].addPoint({y:parseFloat(data.temperature.toFixed(2)) ,x: (data.timestamp-18000) * 1000 },
        true, shift.value);
        tempChart.value.series[1].addPoint({y:parseFloat(data.heatindex.toFixed(2)) ,x: (data.timestamp-18000) * 1000 },
        true, shift.value);
        HiChart.value.series[0].addPoint({y:parseFloat(data.humidity.toFixed(2)) ,x: (data.timestamp-18000)* 1000 },
        true, shift.value);
     
    }else{
        tempChart.value.series[0].addPoint({y:convertToFahrenheit(parseFloat(data.temperature.toFixed(2))) ,x: (data.timestamp-18000) * 1000 },
        true, shift.value);
        tempChart.value.series[1].addPoint({y:convertToFahrenheit(parseFloat(data.heatindex.toFixed(2))) ,x: (data.timestamp-18000) * 1000 },
        true, shift.value);
        HiChart.value.series[0].addPoint({y:parseFloat(data.humidity.toFixed(2)) ,x: (data.timestamp-18000)* 1000 },    
        true, shift.value);
       
}


});

const convertToFahrenheit = (celsius) => {
    return (celsius * 9/5) + 32;
};


function convertTo() {
    // Code to read passcode here
    if(selected.value.includes("Fahrenheit")){
        isCelsius = false;
        tempunits.value = "Fahrenheit";
        tempChart.value.yAxis[0].update({title: { text: '°F' , style:{color:'#000000'}}});
        tempChart.value.yAxis[0].update({labels: { format:'{value} °F' }});
        
    }else if(selected.value.includes("Celsius")){
        isCelsius = true;
        tempunits.value = "Celsius";
        tempChart.value.yAxis[0].update({title: { text: '°C' , style:{color:'#000000'}}});
        tempChart.value.yAxis[0].update({labels: { format:'{value} °C' }});
    }


   
    selected.value = [];
}





</script>


<style scoped>
/** CSS STYLE HERE */

.mb-5 {
    display: flex;
    padding: 0;
    margin: 0;
}
Figure {
border: 2px solid black;
}

.ma-5 {
    font-style: italic;

}

button
{
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto;
    border: 2px solid #f5f5f5;
    color: black;
    font-size: 16px;
    cursor: pointer;
    border-radius: 12px; 
}

.mx-auto {
    display: block;
    color: rgb(255, 255, 255);
    background: rgba(10, 124, 50, 0.581);    
    padding:"25px 50px 75px 100px;"
    
}

.ma-3 {
    display: block;
    padding-left: 150px;
    padding-right: 150px;
    

}

</style>
  