<script setup>
  const props = defineProps({
    visible: {
      type: Boolean,
      default: false,
    },
    text: {
      type: String,
      default: '加载中...',
    },
  })
</script>

<template>
  <div
    v-if="visible"
    class="loading-overlay"
  >
    <!-- 拆分图标和文字，用容器包裹实现并排 -->
    <div class="loading-content">
      <i class="bi bi-arrow-clockwise loading-icon"></i>
      <p class="loading-spinner">
        {{ text }}
      </p>
    </div>
  </div>
</template>

<style scoped lang="scss">
  .loading-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(255, 255, 255, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 9999;
  }

  .loading-content {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    font-size: 24px;
    color: #db729b;
  }

  // 仅让图标旋转
  .loading-icon {
    animation: rotating 2s linear infinite;
  }

  .loading-spinner {
    margin: 0; // 清除p标签默认边距
  }

  @keyframes rotating {
    from {
      transform: rotate(0deg);
    }
    to {
      transform: rotate(360deg);
    }
  }
</style>
