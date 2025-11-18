<script setup>
  import { ref } from 'vue-demi'

  // const mapRef = ref(null)
  // const infoWindowRef = ref(null)
  const center = ref({ lat: 22.745319, lng: 114.965032 })
  const zoom = ref(17)
  const visible = ref(true)

  // 定义信息窗口内容(带样式的HTML字符串)
  const content = ref(`
    <div style="
      width: 150px; 
      white-space: normal;
      font-size: 12px;
    ">
      惠东县黄埠镇综合第二市场
    </div>
  `)
  // const onMapInited = () => {
  //   // 地图加载完成后，可以获取地图实例、窗口实例，调用地图实例、窗口实例方法
  //   console.log(mapRef.value.map)
  //   console.log(infoWindowRef.value.infoWindow)
  // }

  const control = {
    scale: {},
    zoom: {
      position: 'topRight',
    },
  }
</script>

<template>
  <div class="map-wrapper">
    <tlbs-map
      ref="mapRef"
      api-key="OB4BZ-D4W3U-B7VVO-4PJWW-6TKDJ-WPB77"
      :center="center"
      :zoom="zoom"
      :control="control"
    >
      <tlbs-info-window
        ref="infoWindowRef"
        :visible="visible"
        :position="center"
        :content="content"
        :options="{
          offset: {
            x: 0,
            y: 0,
          },
        }"
      />
    </tlbs-map>
  </div>
</template>
<style scoped lang="scss">
  .map-wrapper {
    width: 85%;
    border: 1px solid #ddd;
    margin: 5px auto;
  }

  @media screen and (max-width: 768px) {
    .map-wrapper {
      width: 95%;
      margin: 5px auto;
    }

    .control-container {
      button {
        padding: 2px 4px;
        font-size: 10px;
      }
    }
  }

  @media screen and (max-width: 768px) {
    .map-wrapper {
      width: 95%;
      margin: 5px auto;
      .control-container {
        button {
          padding: 2px 4px;
          font-size: 14px;
        }
      }
      :deep(.tmap-zoom-control) {
        display: none;
      }
      :deep(.rotate-circle) {
        display: none;
      }
    }
  }
</style>
