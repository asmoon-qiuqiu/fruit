<script setup>
  import { ref, computed } from 'vue'
  // 2.分页相关逻辑
  const currentPage = ref(1) // 当前页码
  const pageSize = ref(6) // 每页显示数量
  const jumpPageInput = ref('') //用于存储跳转输入框的值

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
      currentPage.value = page // 转递新的页码
      jumpPageInput.value = '' // 跳转后清空输入框
      // 切换页码后滚动到水果列表顶部
      const fruitList = document.querySelector('.fruit-list')
      if (fruitList) {
        fruitList.scrollIntoView({ behavior: 'smooth', block: 'start' })
      }
    }
  }
  // 跳转处理函数
  const handleJumpPageInput = () => {
    const page = parseInt(jumpPageInput.value)
    if (!isNaN(page)) {
      changePage(page)
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
        <li
          class="list"
          v-for="fruit in paginatedFruits"
          :key="fruit.id"
        >
          <div class="fruit-card">
            <img
              :src="fruit.image"
              :alt="fruit.name"
              class="fruit-img"
            />

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
        <button
          class="page-btn"
          :disabled="currentPage === 1"
          @click="changePage(currentPage - 1)"
        >
          <i class="bi bi-chevron-left"></i>
        </button>
        <!-- 页码 -->
        <button
          class="page-number"
          :class="{ active: page === currentPage, ellipsis: page === '...' }"
          :disabled="page === '...'"
          v-for="(page, index) in pageNumbers"
          :key="index"
          @click="page !== '...' && changePage(page)"
        >
          {{ page }}
        </button>
        <!-- 下一页 -->
        <button
          class="page-btn"
          :disabled="currentPage === totalPages"
          @click="changePage(currentPage + 1)"
        >
          <i class="bi bi-chevron-right"></i>
        </button>
        <!-- 跳转输入框 -->
        <div class="page-jump">
          <span>跳转到</span>
          <input
            type="number"
            min="1"
            :max="totalPages"
            v-model="jumpPageInput"
            @keyup.enter="handleJumpPageInput"
          />
          <span>页</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
  .main {
    display: flex;
    flex-wrap: wrap;
    align-items: flex-start; // 顶部对齐
    padding-left: 10px;
    background: url(../../public/images/main.jpg) no-repeat center;
    background-size: cover;
    background-attachment: fixed;
    h2 {
      color: #c2185b;
      margin: 15px 0;
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
          background-color: #c2185b;
          border-color: #c2185b;
          color: #fff;
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
  }
</style>
