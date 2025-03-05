<template>
  
  <VContainer class="fill-height ">
    <VResponsive class="align-center text-center fill-height">
      <VImg height="350" class="mb-5" src="@/assets/iotFarming.svg" />

      <div class="text-body-2 font-weight-light mb-n1">DefCon4 Presents</div>

      <h1 class="text-h2 font-weight-bold">Smart Farming Solutions</h1>
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
