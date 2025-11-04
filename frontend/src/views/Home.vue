<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
// 控制返回顶部按钮显示/隐藏的状态（默认隐藏）
const showBackTop = ref(false)

// 滚动到顶部的方法
const scrollToTop = () => {
    window.scrollTo({
        top: 0, // 滚动到页面顶部
        behavior: 'smooth' // 平滑滚动效果
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
    <!-- 头部导航 -->
    <Header></Header>

    <!-- 轮播图 -->
    <div class="banner">
        <div id="carouselExampleFade" class="carousel slide" data-bs-ride="carousel" data-bs-interval="2000"
            data-bs-scroll="false">
            <div class="carousel-inner">
                <!-- 轮播项图片替换 -->
                <div class="carousel-item active">
                    <img src="../../public/images/fruit-image1.png" class="d-block w-100" alt="水果轮播图1">
                </div>
                <div class="carousel-item">
                    <img src="../../public/images/fruit-image1.png" class="d-block w-100" alt="水果轮播图2">
                </div>
                <div class="carousel-item">
                    <img src="../../public/images/fruit-image1.png" class="d-block w-100" alt="水果轮播图3">
                </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade"
                data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade"
                data-bs-slide="next">
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
        </div>
        <div class="fruit-list">
            <!-- 苹果列表 -->
            <ul>
                <li class="list">
                    <div class="fruit-card">
                        <img src="https://picsum.photos/id/1080/300/200" alt="红苹果" class="fruit-img">
                        <div class="fruit-info">
                            <h3>红富士苹果</h3>
                            <p>脆甜多汁，富含维生素C，适合直接食用或制作沙拉。</p>
                            <span class="price">¥8.9/斤</span>
                        </div>
                    </div>
                </li>

                <li class="list">
                    <div class="fruit-card">
                        <img src="https://picsum.photos/id/1065/300/200" alt="青苹果" class="fruit-img">
                        <div class="fruit-info">
                            <h3>青苹果</h3>
                            <p>酸甜可口，富含膳食纤维，有助于消化。</p>
                            <span class="price">¥7.5/斤</span>
                        </div>
                    </div>
                </li>

                <li class="list">
                    <div class="fruit-card">
                        <img src="https://picsum.photos/id/1065/300/200" alt="青苹果" class="fruit-img">
                        <div class="fruit-info">
                            <h3>青苹果</h3>
                            <p>酸甜可口，富含膳食纤维，有助于消化。</p>
                            <span class="price">¥7.5/斤</span>
                        </div>
                    </div>
                </li>

                <li class="list">
                    <div class="fruit-card">
                        <img src="https://picsum.photos/id/1065/300/200" alt="青苹果" class="fruit-img">
                        <div class="fruit-info">
                            <h3>青苹果</h3>
                            <p>酸甜可口，富含膳食纤维，有助于消化。</p>
                            <span class="price">¥7.5/斤</span>
                        </div>
                    </div>
                </li>
                <li class="list">
                    <div class="fruit-card">
                        <img src="https://picsum.photos/id/1065/300/200" alt="青苹果" class="fruit-img">
                        <div class="fruit-info">
                            <h3>青苹果</h3>
                            <p>酸甜可口，富含膳食纤维，有助于消化。</p>
                            <span class="price">¥7.5/斤</span>
                        </div>
                    </div>
                </li>
                <li class="list">
                    <div class="fruit-card">
                        <img src="https://picsum.photos/id/1065/300/200" alt="青苹果" class="fruit-img">
                        <div class="fruit-info">
                            <h3>青苹果</h3>
                            <p>酸甜可口，富含膳食纤维，有助于消化。</p>
                            <span class="price">¥7.5/斤</span>
                        </div>
                    </div>
                </li>

            </ul>
        </div>

        <div class="rside">
            <div class="search-container">
                <form action="#">
                    <input type="text" placeholder="搜索.." name="search">
                    <button type="submit"><i class="bi bi-search"></i></button>
                </form>
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
        color: #C2185B;
        margin: 20px 0;
        padding-left: 5px;
    }

    .tab {
        flex: 0 0 15%;
        border: 1px solid #e0f2e9;
        background-color: #FFF0F5;
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
            font-size: 17px;
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
        padding-left: 20px;
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
                            margin-top: 5px;
                        }

                        p {
                            font-size: 14px;
                        }
                    }

                    .fruit-img {
                        width: 100%;
                        height: auto;
                        object-fit: cover;
                        border-radius: 5px;
                    }
                }
            }
        }

    }

    .rside {
        flex: 0 0 300px; // 固定宽度，不缩放
        padding: 0 20px 0 20px;
        margin-top: 20px;

        .search-container {
            background-color: #f0fdf4;
            padding: 10px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);

            form {
                display: flex;
                align-items: center;

                input[type="text"] {
                    flex: 1;
                    padding: 8px;
                    border: 1px solid #ddd;
                    border-radius: 4px 0 0 4px;
                    outline: none;
                    font-size: 14px;
                }

                button {
                    padding: 8px 12px;
                    background-color: #24f563;
                    color: #333;
                    border: none;
                    border-radius: 0 4px 4px 0;
                    cursor: pointer;
                    transition: background-color 0.3s;

                    &:hover {
                        background-color: #34ca61;
                    }

                    i {
                        font-size: 14px;
                    }
                }
            }
        }
    }

    @media screen and (max-width: 1200px) {
        padding: 0;

        .tab {
            flex: 0 0 100%;
            margin-top: 0;
            height: auto;
        }

        .tab button {
            display: inline-block;
            width: auto;
            margin: 10px;
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
                content: "";
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
    .main {
        padding: 0;

        .fruit-list {
            padding: 0;

            ul {
                grid-template-columns: repeat(1, 1fr);

                .list .fruit-card {
                    .fruit-img {
                        width: 100%;
                        height: 200px;
                        object-fit: cover;
                        border-radius: 4px;
                    }
                }

            }
        }

        .rside {
            margin-bottom: 100px;
        }
    }

    /* 小屏幕下“返回顶部”按钮优化 */
    .back-to-top {
        // 小屏幕下保持按钮显示（移除原 display: none）
        width: 40px;
        height: 40px;
        bottom: 10%;
        right: 20px;

        .bi {
            font-size: 18px;
        }

        .text {
            font-size: 12px;
            padding: 3px 6px;
            bottom: 30px; // 调整提示文本垂直位置
        }

    }
}
</style>
