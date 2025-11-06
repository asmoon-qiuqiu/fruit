<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
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

// 2.分页相关逻辑
const currentPage = ref(1) // 当前页码
const pageSize = ref(6) // 每页显示数量

// 模拟水果数据（后续从接口获取）
const allFruits = ref([
  {
    id: 1,
    name: '红富士苹果',
    desc: '脆甜多汁，富含维生素C，适合直接食用或制作沙拉。',
    price: '8.9',
    image: 'https://picsum.photos/id/1080/300/200',
  },
  {
    id: 2,
    name: '青苹果',
    desc: '酸甜可口，富含膳食纤维，有助于消化。',
    price: '7.5',
    image: 'https://picsum.photos/id/1065/300/200',
  },
  {
    id: 3,
    name: '香蕉',
    desc: '香甜软糯，富含钾元素，补充能量。',
    price: '5.9',
    image: 'https://picsum.photos/id/1060/300/200',
  },
  {
    id: 4,
    name: '橙子',
    desc: '酸甜多汁，维生素C含量丰富。',
    price: '6.8',
    image: 'https://picsum.photos/id/1061/300/200',
  },
  {
    id: 5,
    name: '西瓜',
    desc: '清甜解暑，夏日必备水果。',
    price: '3.5',
    image: 'https://picsum.photos/id/1062/300/200',
  },
  {
    id: 6,
    name: '葡萄',
    desc: '颗粒饱满，酸甜适中，营养丰富。',
    price: '12.9',
    image: 'https://picsum.photos/id/1063/300/200',
  },
  {
    id: 7,
    name: '草莓',
    desc: '鲜红欲滴，香甜可口，维C之王。',
    price: '15.9',
    image: 'https://picsum.photos/id/1064/300/200',
  },
  {
    id: 8,
    name: '芒果',
    desc: '香甜多汁，果肉细腻，热带风味。',
    price: '9.9',
    image: 'https://picsum.photos/id/1066/300/200',
  },
  {
    id: 9,
    name: '猕猴桃',
    desc: '酸甜爽口，维生素含量极高。',
    price: '8.5',
    image: 'https://picsum.photos/id/1067/300/200',
  },
  {
    id: 10,
    name: '火龙果',
    desc: '清甜爽口，富含花青素，美容养颜。',
    price: '7.9',
    image: 'https://picsum.photos/id/1068/300/200',
  },
  {
    id: 11,
    name: '荔枝',
    desc: '甜美多汁，果肉晶莹剔透。',
    price: '18.9',
    image: 'https://picsum.photos/id/1069/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
  {
    id: 12,
    name: '樱桃',
    desc: '小巧玲珑，酸甜可口，营养价值高。',
    price: '25.9',
    image: 'https://picsum.photos/id/1070/300/200',
  },
])
// 计算总页数
const totalPages = computed(() => {
  return Math.ceil(allFruits.value.length / pageSize.value)
})

// 计算当前页显示的水果数据
const paginatedFruits = computed(() => {
  const start = (currentPage.value - 1) * pageSize.value
  const end = start + pageSize.value
  return allFruits.value.slice(start, end)
})

// 切换页码
const changePage = (page) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page
    // 切换页码后滚动到水果列表顶部
    const fruitList = document.querySelector('.fruit-list')
    if (fruitList) {
      fruitList.scrollIntoView({ behavior: 'smooth', block: 'start' })
    }
  }
}

// 生成页码数组（最多显示5个页码）
const pageNumbers = computed(() => {
  const pages = []
  const total = totalPages.value
  const current = currentPage.value

  if (total <= 5) {
    // 总页数小于等于5，全部显示
    for (let i = 1; i <= total; i++) {
      pages.push(i)
    }
  } else {
    // 总页数大于5，显示省略号
    if (current <= 3) {
      // 当前页在前面
      pages.push(1, 2, 3, 4, '...', total)
    } else if (current >= total - 2) {
      // 当前页在后面
      pages.push(1, '...', total - 3, total - 2, total - 1, total)
    } else {
      // 当前页在中间
      pages.push(1, '...', current - 1, current, current + 1, '...', total)
    }
  }
  return pages
})
</script>

<template>
  <!-- 头部导航 -->
  <Header></Header>

  <!-- 轮播图 -->
  <div class="banner">
    <div id="carouselExampleFade" class="carousel slide" data-bs-ride="carousel" data-bs-interval="2000"
      data-bs-scroll="false">
      <div class="carousel-inner">
        <!-- 轮播项图片替换 -->
        <div class="carousel-item active">
          <img src="../../public/images/fruit-image1.png" class="d-block w-100" alt="水果轮播图1" />
        </div>
        <div class="carousel-item">
          <img src="../../public/images/fruit-image1.png" class="d-block w-100" alt="水果轮播图2" />
        </div>
        <div class="carousel-item">
          <img src="../../public/images/fruit-image1.png" class="d-block w-100" alt="水果轮播图3" />
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>

  <!-- 内容 -->
  <div class="main">
    <div class="tab">
      <h2>水果目录</h2>
      <button class="tablinks">苹果</button>
      <button class="tablinks">香蕉</button>
      <button class="tablinks">西瓜</button>
      <button class="tablinks">西瓜</button>
      <button class="tablinks">西瓜</button>
      <button class="tablinks">西瓜</button>
    </div>

    <!-- 水果列表 -->
    <div class="fruit-list">
      <ul>
        <li class="list" v-for="fruit in paginatedFruits" :key="fruit.id">
          <div class="fruit-card">

            <img :src="fruit.image" :alt="fruit.name" class="fruit-img" />

            <div class="fruit-info">
              <h3>{{ fruit.name }}</h3>
              <p>{{ fruit.desc }}</p>
              <span class="price">¥{{ fruit.price }}/斤</span>
            </div>

          </div>
        </li>
      </ul>
      <!-- 分页模块 -->
      <div class="pagination">
        <!-- 上一页 -->
        <button class="page-btn" :disabled="currentPage === 1" @click="changePage(currentPage - 1)">
          <i class="bi bi-chevron-left"></i>
        </button>
        <!-- 页码 -->
        <button class="page-number" :class="{ active: page === currentPage, ellipsis: page === '...' }"
          v-for="(page, index) in pageNumbers" :key="index" :disabled="page === '...'"
          @click="page !== '...' && changePage(page)">
          {{ page }}
        </button>
        <!-- 下一页 -->
        <button class="page-btn" :disabled="currentPage === totalPages" @click="changePage(currentPage + 1)">
          <i class="bi bi-chevron-right"></i>
        </button>
        <!-- 跳转输入框 -->
        <div class="page-jump">
          <span>跳转到</span>
          <input type="number" min="1" :max="totalPages" v-model.number="currentPage"
            @keyup.enter="changePage(currentPage)" />
          <span>页</span>
        </div>
      </div>
    </div>
  </div>

  <!-- 底部 -->
  <Footer></Footer>

  <!-- 返回顶部按钮：默认隐藏，滚动到指定高度显示 -->
  <button class="back-to-top" v-show="showBackTop" @click="scrollToTop">
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

.main {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start; // 顶部对齐
  padding-left: 10px;
  background: url(../../public/images/preview1.jpg) no-repeat center;
  background-size: cover;

  h2 {
    color: #c2185b;
    margin: 20px 0;
    padding-left: 5px;
  }

  .tab {
    flex: 0 0 15%;
    border: 1px solid #e0f2e9;
    background-color: #fff0f5;
    height: auto;
    margin-top: 20px;
    padding: 0 5px;
    opacity: 0.9;

    .tablinks {
      display: block;
      background-color: #fff;
      color: #f97316;
      padding: 20px 15px;
      width: 100%;
      border: none;
      text-align: center;
      transition: 0.3s;
      font-size: 18px;
      margin: 10px 0;
      border-radius: 5px;
      cursor: pointer;

      &:hover {
        background-color: #fff7ed;
        color: #ea580c;
      }

      &:active {
        background-color: #f97316;
        color: #fff;
      }
    }
  }

  .fruit-list {
    flex: 1;
    padding: 0 20px 20px 20px;

    margin-top: 20px;

    ul {
      padding: 0;
      display: grid; // 网格布局
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;

      .list {
        list-style-type: none;
        width: 100%;

        .fruit-card {
          border: 1px solid #eee;
          border-radius: 8px;
          box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);

          .fruit-info {
            padding: 0 0 10px 10px;

            h3 {
              font-size: 20px;
              margin-top: 10px;
            }

            p {
              font-size: 14px;
              margin: 0;
            }
          }

          .fruit-img {
            width: 100%;
            height: 250px;
            object-fit: cover;
            border-radius: 5px;
          }
        }
      }
    }
  }

  // 分页样式
  .pagination {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 8px;
    margin-top: 40px;
    padding: 20px 0;

    .page-btn,
    .page-number {
      min-width: 40px;
      height: 40px;
      border: 1px solid #ddd;
      background-color: #fff;
      color: #c2185b;
      border-radius: 5px;
      cursor: pointer;
      transition: all 0.3s;
      font-size: 14px;

      &:hover:not(:disabled):not(.ellipsis) {
        background-color: #fff0f5;
        border-color: #c2185b;
        color: #c2185b;
      }

      &:disabled {
        cursor: not-allowed;
        opacity: 0.5;
      }

      &.active {
        background-color: #c2185b;
        color: #fff;
        border-color: #c2185b;
      }

      &.ellipsis {
        border: none;
        cursor: default;
        background: transparent;
      }
    }

    .page-jump {
      display: flex;
      align-items: center;
      gap: 5px;
      margin-left: 15px;
      font-size: 14px;
      color: #c2185b;

      input {
        width: 40px;
        height: 20px;
        border: 1px solid #ddd;
        border-radius: 4px;
        text-align: center;
        font-size: 14px;
        outline: none;

        &:focus {
          border-color: #c2185b;
        }

        // 移除数字输入框的上下箭头
        &::-webkit-inner-spin-button,
        &::-webkit-outer-spin-button {
          -webkit-appearance: none;
          margin: 0;
        }
      }
    }
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

@media screen and (max-width: 1200px) {
  .main {
    padding: 0;

    .tab {
      display: flex;
      flex: 0 0 100%;
      flex-wrap: wrap;
      margin-top: 0;

      h2 {
        width: 100%;
        white-space: nowrap;
        padding-left: 5px;
        margin: 20px 0;
      }

      .tablinks {
        display: flex;
        justify-content: center;
        align-items: center;
        min-width: 120px;
        flex: 1 1 calc(25% - 10px);
        height: 50px;
        margin: 5px;
      }
    }

    .rside {
      flex: 0 0 100%;
      margin-bottom: 10px;
    }

    .fruit-list {
      padding: 10px;

      ul {
        grid-template-columns: repeat(2, 1fr);
        padding: 5px;
      }
    }
  }
}

@media screen and (max-width: 600px) {
  .main {
    padding-top: 45px;

    .fruit-list {
      padding: 0;
      margin-bottom: 50px;

      ul {
        grid-template-columns: repeat(2, 1fr);
        gap: 5px;
        padding: 0;
        margin: 0;

        .list .fruit-card {
          margin: 0 5px 0 5px;

          .fruit-img {
            width: 100%;
            height: auto;
            object-fit: cover;
            border-radius: 4px;
          }

          .fruit-info {
            h3 {
              font-size: 14px;
              font-weight: bold;
            }

            p {
              font-size: 12px;
              font-weight: bold;
            }

            .price {
              font-size: 12px;
              padding-left: 2px;
              font-weight: bold;
            }
          }
        }
      }
    }

    // 分页
    .pagination {
      flex-wrap: wrap;
      margin-top: 10px;
      margin-bottom: 10px;

      .page-btn,
      .page-number {
        min-width: 30px;
        height: 30px;
        font-size: 12px;
      }

      .page-jump {
        font-size: 12px;
        margin-left: 5px;
      }
    }

    .rside {
      margin-bottom: 100px;
    }
  }



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
