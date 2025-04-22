<template>
    <v-container class="py-5">
        <v-row justify="center">
            <v-col cols="12" sm="8" md="6">
                <v-card class="elevation-3">
                    <v-card-title class="text-h5 text-center color-primary">
                        Real-Time Weather
                    </v-card-title>
                    <v-card-text>
                        <v-text-field
                            v-model="cityName"
                            label="Enter a location"
                            outlined
                            dense
                        ></v-text-field>
                        <v-btn
                            @click="getWeather"
                            color="primary"
                            block
                            class="my-3"
                        >
                            Get Weather
                        </v-btn>
                        <v-divider></v-divider>
                        <v-alert
                            v-if="error"
                            type="error"
                            class="mt-3"
                            dense
                        >
                            {{ error }}
                        </v-alert>
                        <div v-if="weatherData" class="mt-4">
                            <p class="text-body-1">
                                <strong>Location:</strong>
                                <span class="text-primary">{{ weatherData.name }}</span>
                            </p>
                            <p class="text-body-1">
                                <strong>Temperature:</strong>
                                <span class="text-danger">{{ weatherData.main.temp }}</span> °C
                            </p>
                            <p class="text-body-1">
                                <strong>Min Temp:</strong>
                                <span class="text-primary">{{ weatherData.main.temp_min }}</span> °C
                            </p>
                            <p class="text-body-1">
                                <strong>Max Temp:</strong>
                                <span class="text-danger">{{ weatherData.main.temp_max }}</span> °C
                            </p>
                            <p class="text-body-1">
                                <strong>Heat Index:</strong>
                                <span class="text-primary">{{ weatherData.main.feels_like }}</span> °C
                            </p>
                            <p class="text-body-1">
                                <strong>Humidity:</strong>
                                <span class="text-danger">{{ weatherData.main.humidity }}</span> %
                            </p>
                            <p class="text-body-1">
                                <strong>Pressure:</strong>
                                <span class="text-primary">{{ weatherData.main.pressure }}</span> hPa
                            </p>
                        </div>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from "vue";
import { useMqttStore } from "@/store/mqttStore";
import { storeToRefs } from "pinia";

const Mqtt = useMqttStore();
const { payload, payloadTopic } = storeToRefs(Mqtt);

const cityName = ref("");
const error = ref("");
const weatherData = ref(null);
const apiKey = "ec93b156a9d6f88b5c58b38d2c0d783f";

onMounted(() => {
    Mqtt.connect();
    setTimeout(() => {
        Mqtt.subscribe("620157646");
        Mqtt.subscribe("620157646_pub");
    }, 3000);
});

onBeforeUnmount(() => {
    Mqtt.unsubcribeAll();
});

const getWeather = async () => {
    try {
        const response = await fetch(
            `http://api.openweathermap.org/data/2.5/weather?q=${cityName.value}&units=metric&appid=${apiKey}`
        );
        if (!response.ok) throw new Error("Failed to fetch weather data");
        weatherData.value = await response.json();
        error.value = "";
    } catch (err) {
        console.error(err);
        error.value = "Failed to fetch weather data";
        weatherData.value = null;
    }
};
</script>

<style scoped>
.primary--text {
    color: #6200ea !important;
}
.text-primary {
    color: #1976d2;
}
.text-danger {
    color: #d32f2f;
}
</style>