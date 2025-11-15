<script setup>
  import { ref, onMounted, onUnmounted } from 'vue'
  import MainFruits from '@/components/MainFruits.vue'
  // 1.控制返回顶部按钮显示/隐藏的状态（默认隐藏）
  const showBackTop = ref(false)

  // 滚动到顶部的方法
  const scrollToTop = () => {
    window.scrollTo({
      top: 0, // 滚动到页面顶部
      behavior: 'smooth', // 平滑滚动效果
    })
  }

  // 监听页面滚动事件的处理函数
  const handleScroll = () => {
    // 当页面滚动距离顶部超过 150px 时，显示按钮
    showBackTop.value = window.pageYOffset > 150
  }

  // 页面挂载时添加滚动监听
  onMounted(() => {
    window.addEventListener('scroll', handleScroll)
  })

  // 页面卸载时移除滚动监听（避免内存泄漏）
  onUnmounted(() => {
    window.removeEventListener('scroll', handleScroll)
  })
</script>

<template>
  <!-- 轮播图 -->
  <div class="banner">
    <div
      id="carouselExampleFade"
      class="carousel slide"
      data-bs-ride="carousel"
      data-bs-interval="2000"
      data-bs-scroll="false"
    >
      <div class="carousel-inner">
        <!-- 轮播项图片替换 -->
        <div class="carousel-item active">
          <img
            src="../../public/images/fruit-image1.png"
            class="d-block w-100"
            alt="水果轮播图1"
          />
        </div>
        <div class="carousel-item">
          <img
            src="../../public/images/about.jpg"
            class="d-block w-100"
            alt="水果轮播图2"
          />
        </div>
        <div class="carousel-item">
          <img
            src="../../public/images/fruit-image1.png"
            class="d-block w-100"
            alt="水果轮播图3"
          />
        </div>
      </div>
      <button
        class="carousel-control-prev"
        type="button"
        data-bs-target="#carouselExampleFade"
        data-bs-slide="prev"
      >
        <span
          class="carousel-control-prev-icon"
          aria-hidden="true"
        ></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button
        class="carousel-control-next"
        type="button"
        data-bs-target="#carouselExampleFade"
        data-bs-slide="next"
      >
        <span
          class="carousel-control-next-icon"
          aria-hidden="true"
        ></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>

  <!-- 内容 -->
  <MainFruits></MainFruits>

  <!-- 返回顶部按钮：默认隐藏，滚动到指定高度显示 -->
  <button
    class="back-to-top"
    v-show="showBackTop"
    @click="scrollToTop"
  >
    <div class="tooltip-text">
      <!-- 上方弹出的文字提示 -->
      <span class="text">返回顶部</span>
      <i class="bi bi-arrow-up"></i>
    </div>
  </button>
</template>

<style scoped lang="scss">
  .banner {
    height: 607px !important;
    overflow: hidden;
    position: relative;
    min-height: 607px !important;
    max-height: 607px !important; // 严格限制最大高度
    display: block; // 改为 block，避免 flex 影响

    .carousel {
      height: 607px !important;
      min-height: 607px !important;
      max-height: 607px !important;
      margin: 0;
      padding: 0;
    }

    .carousel-inner {
      height: 607px !important;
      min-height: 607px !important;
      max-height: 607px !important;
      margin: 0;
      padding: 0;
      position: relative;
      overflow: hidden;
    }

    .carousel-item {
      height: 607px !important;
      min-height: 607px !important;
      max-height: 607px !important;
      margin: 0;
      padding: 0;
      // 关键修改：使用绝对定位让所有轮播项叠加
      position: absolute !important;
      top: 0;
      left: 0;
      width: 100%;

      // 确保切换过程中的状态也保持固定高度
      &.active {
        display: block !important;
        height: 607px !important;
      }
    }

    // 给轮播图片添加固定高度
    .carousel-item img {
      height: 607px !important;
      width: 100% !important;
      min-height: 607px !important;
      max-height: 607px !important;
      object-fit: cover;
      background-color: #f5f5f5;
      display: block !important; // 移除图片底部间隙
      margin: 0;
      padding: 0;
    }

    .carousel-control-prev,
    .carousel-control-next {
      width: 50px;
      height: 50px;
      top: 50%;
      transform: translateY(-50%);
      background-color: rgba(255, 255, 255, 0.6);
      border-radius: 50%;
      padding: 0;
      margin: 0 5px 0 0;
      z-index: 10; // 确保按钮在最上层

      .carousel-control-prev-icon,
      .carousel-control-next-icon {
        width: 25px;
        height: 20px;
        background-size: 100%;
      }
    }

    @media screen and (max-width: 600px) {
      display: none;
    }
  }

  /* 返回顶部按钮样式 */
  .back-to-top {
    position: fixed; // 固定定位，不随页面滚动
    bottom: 30px; // 距离页面底部 30px
    right: 30px; // 距离页面右侧 30px
    width: 45px;
    height: 45px;
    border-radius: 50%; // 圆形按钮
    background-color: #fff0f5; // 与头部同色系，保持风格统一
    border: none;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2); // 阴影增强层次感
    cursor: pointer;
    transition: background-color 0.3s; //  hover 过渡效果

    &:hover {
      background-color: #c2185c9c; //  hover 时加深颜色
    }

    // 上方文字
    .tooltip-text {
      position: relative;

      .bi {
        font-size: 20px; // 图标大小
      }

      .text {
        position: absolute;
        bottom: 35px;
        left: 50%;
        transform: translateX(-50%);
        white-space: nowrap;
        margin-bottom: 10px;
        font-size: 14px;
        background-color: #c2185b;
        color: white;
        border-radius: 4px;
        padding: 4px 8px;
        pointer-events: none;
        opacity: 0;
        transition: all 0.3s ease;

        &::after {
          content: '';
          position: absolute;
          top: 100%;
          left: 50%;
          transform: translateX(-50%);
          border-width: 5px;
          border-style: solid;
          border-color: #c2185b transparent transparent transparent;
        }
      }
    }

    &:hover .text {
      opacity: 1;
    }

    &:hover .bi {
      color: #fff;
    }
  }

  @media screen and (max-width: 600px) {
    /* 小屏幕下“返回顶部”按钮优化 */
    .back-to-top {
      width: 30px;
      height: 30px;
      bottom: 10%;
      right: 20px;

      .bi {
        font-size: 12px;
      }

      .text {
        display: none;
      }
    }
  }
</style>
