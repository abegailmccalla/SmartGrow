<template>
  
  <VContainer class="fill-height ">
    <VResponsive class="align-center text-center fill-height">
      <VImg height="350" class="mb-5" src="@/assets/iotFarming.svg" />

      <div class="text-body-2 font-weight-light mb-n1">DefCon4 Presents</div>

      <h1 class="text-h2 font-weight-bold" id="title">SmartGrow</h1><br>
      <div class="text-container">
        <h2>Introducing <span style="color: #4CAF50;">SmartGrow</span> the future of effortless farming!</h2>
        <p>
            With intelligent automation, real-time monitoring, and precision-controlled fertilization, 
            <span style="color: #4CAF50;">SmartGrow</span> maximizes growth while minimizing effort.
        </p>
      </div><br><br>


      <div class="text-body-1 font-weight-heavy mt-1">Team Members</div><br>
      <div class="d-flex justify-center">
        <div class="text-body-1 font-weight-light mt-1 mx-2">Fabari Williams</div>
        <div class="text-body-1 font-weight-light mt-1 mx-2">Abegail McCalla</div>
        <div class="text-body-1 font-weight-light mt-1 mx-2">Joel Foster</div>
        <div class="text-body-1 font-weight-light mt-1 mx-2">Jeroen Wong</div>
      </div>
      

      <div class="py-14" />

   
    </VResponsive>
  </VContainer>

</template>

<script setup>
  import { storeToRefs } from 'pinia';
  import { useMqttStore } from '@/store/mqttStore';
  import { ref,reactive, watch, onMounted, onBeforeUnmount } from 'vue';


// VARIABLES


// FUNCTIONS
onMounted(()=>{
   
});

onBeforeUnmount(()=>{ 
  
});
</script>
<style>
body {
    font-family: Arial, sans-serif;
    text-align: center;
    padding: 20px;
    background-color: #f4f4f4;
}
.text-container h2, .text-container p {
    opacity: 0;
    transform: translateY(20px);
    animation: fadeInUp 1s ease-out forwards;
}
.text-container p {
    animation-delay: 0.5s; /* Delays paragraph reveal slightly */
}

#title {
    text-shadow: 0 0 10px rgba(76, 175, 80, 0.6);
}


@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
        filter: blur(5px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
        filter: blur(0);
    }

}
</style>