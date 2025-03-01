<template>
    <v-container class="bg-surface mb-6" align="center">
        <v-sheet class="pb-2 mb-2" color="surface" rounded="xl" align="center">
           
            <v-row :max-width="1000">
                <v-col class="d-flex justify-center">
                    <v-sheet class="d-inline justify-center">
                        <v-row>
                            <v-col>
                                <v-card :width="300" :height="200" class="text-secondary" color="surface">
                                    <v-card-title>
                                        <v-icon left>mdi-cloud</v-icon>
                                        Inside Environment
                                    </v-card-title>
                                    <v-card-text>
                                        <v-row class="d-flex justify-space-between px-4 pa-2">
                                            <span class="label">Temperature</span>
                                            <span class="text-h6">{{ temperature }}</span>
                                        </v-row>
                                        <v-row class="d-flex justify-space-between px-4 pa-2">
                                            <span class="label">Humidity</span>
                                            <span class="text-h6">{{ humidity }}</span>
                                        </v-row>
                                        <v-row class="d-flex justify-space-between px-4 pa-2">
                                            <span class="label">Heat Index</span>
                                            <span class="text-h6">{{ heatindex }}</span>
                                        </v-row>
                                    </v-card-text>
                                </v-card><br>
                            
                                <v-card :width="300" :height="200" class="text-secondary" color="surface">
                                    <v-card-title>
                                       
                                        Fan Status
                                    </v-card-title>
                                    <v-card-text>
                                        <v-spacer></v-spacer>
                                        <div class="status-indicator">
                                            <v-icon size="100" color="primary" class="mdi-spin">mdi-fan</v-icon>

                                        </div>
                                    </v-card-text>
                                    <span class="status">{{ fanStatus ? 'Active' : 'Inactive' }}</span>
                                    </v-card>
                            </v-col>
                        </v-row>
                    </v-sheet>
                </v-col>
                <v-col cols="2">
                    <v-sheet>
                        <v-card height="360px" width="175px" elevation="0">
                            <v-slider class="slider" readonly thumb-label color="blue" v-model="waterSlider" direction="vertical" label="Water Reservoir" track-size="50">
                            </v-slider>
                        </v-card>
                    </v-sheet>
                </v-col>
                <v-col cols="2">
                    <v-sheet>
                        <v-card height="360px" width="175px" elevation="0">
                            <v-slider class="slider" readonly thumb-label color="teritiary" v-model="fertilizerSlider" direction="vertical" label="Fertilizer Tray" track-size="50">
                            </v-slider>
                        </v-card>
                    </v-sheet>
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
 
 
// VARIABLES
const router      = useRouter();
const route       = useRoute();  
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
const fanStatus = ref(true); // Fan status
let moist = ref(10); // soil moisture
let tankLevel = ref(10); // tank level
const selected = ref([]); // Selected units
const led = reactive({"brightness":255,"nodes":1,"color":{ r: 45, g: 120, b: 150, a: 1 }});
let timer, ID = 1000;
const indicatorColor = computed(()=>{
    return `rgba(${led.color.r},${led.color.g},${led.color.b},${led.color.a})`
});

const fertilizerSlider = ref(50);
const waterSlider = ref(50);


const temperature = computed(()=>{
    if(!!payload.value){
        if(isCelsius){
            return `${payload.value.temperature.toFixed(2)} °C`;
        }else{
            return `${convertToFahrenheit(payload.value.temperature).toFixed(2)} °F`;
        }
    }
});
const heatindex = computed(()=>{
    if(!!payload.value){
        if(isCelsius){
            return `${payload.value.heatindex.toFixed(2)} °C`;
        }else{
            return `${convertToFahrenheit(payload.value.heatindex).toFixed(2)} °F`;
        }
    }
});
const humidity = computed(()=>{
    if(!!payload.value){
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

    waterSlider.value = data.tank;
    fertilizerSlider.value = data.tank
    
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
  