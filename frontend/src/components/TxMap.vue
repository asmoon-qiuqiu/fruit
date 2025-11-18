<script setup>
  import { ref } from 'vue-demi'

  // const mapRef = ref(null)
  // const infoWindowRef = ref(null)
  const center = ref({ lat: 22.745319, lng: 114.965032 })
  const zoom = ref(17)
  const visible = ref(true)

  const switchInfoWindow = () => {
    visible.value = !visible.value
  }
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
  // // 地图加载完成后，可以获取地图实例、窗口实例，调用地图实例、窗口实例方法
  // const onMapInited = () => {
  //   console.log(infoWindowRef.value.infoWindow)
  // }
  // 如果需要在地图初始化后做某些操作，使用 onMounted

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
      <div class="control-container">
        <button @click.stop="switchInfoWindow">{{ visible ? '关闭' : '开启' }}窗口</button>
      </div>
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

  .control-container {
    position: absolute;
    top: 0;
    left: 0;
    z-index: 1000;
    display: flex;
    align-items: center;
    button {
      padding: 1px;
      background-color: #fff;
      margin-right: 5px;
      font-size: 12px;
      border: 1px solid #ddd;
    }
  }
</style>
