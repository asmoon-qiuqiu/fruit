<script setup>
import { ref, onMounted, onUnmounted } from 'vue'


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
    <div class="header">
        <router-link to="/">首页</router-link>
        <a href="#">水果种类</a>
        <a href="#">关于我们</a>
        <a href="#">联系我们</a>
        <a href="#"><i class="bi bi-box-arrow-in-right"></i>登录</a>
    </div>

    <div class="banner">
        <div id="carouselExampleFade" class="carousel slide" data-bs-ride="carousel" data-bs-interval="3000"
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

    <h2>水果目录</h2>
    <div class="main">
        <div class="tab">
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

    <div class="footer">
        <div class="footer-content">
            <p class="footer-addr">地址: 广东省惠州市惠东县黄埠镇</p>
            <p class="footer-email">联系邮箱: 2371824615@qq.com</p>
            <p class="footer-copyright">© 2025 个人制作 版权所有</p>
        </div>
    </div>

    <!-- 返回顶部按钮：默认隐藏，滚动到指定高度显示 -->
    <button class="back-to-top" v-show="showBackTop" @click="scrollToTop">
        <i class="bi bi-arrow-up"></i>
    </button>
</template>

<style scoped lang="scss">
* {
    box-sizing: border-box;
    font-family: Arial, Helvetica, sans-serif;
    margin: 0;
    padding: 0;
}

h2 {
    color: #24f563;
    margin: 20px 0;
    padding-left: 10px;
}

.header {
    background-color: #24f563;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    border-radius: 5px;

    a {
        font-size: 18px;
        padding: 15px;
        text-decoration: none;
        color: #333;

        .bi {
            margin-right: 5px;
        }

        &:hover,
        &:active {
            background-color: #34ca61;
            color: #F5F9FF;
        }
    }

    @media screen and (max-width: 600px) {
        font-size: 18px;
        flex-direction: column;
        align-items: flex-start;
        width: 100vw;
        /* 占满整个视口宽度 */
        min-width: 320px;

        /* 确保在极小屏幕上不被过度压缩 */
        a {

            &:hover,
            &:active {
                background-color: rgba(0, 0, 0, 0);
            }
        }
    }
}

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

    .tab {
        flex: 0 0 15%;
        border: 1px solid #e0f2e9;
        background-color: #f0fdf4;
        height: 250px;

        button {
            display: block;
            background-color: #fff;
            color: #f97316;
            padding: 22px 16px;
            width: 100%;
            border: none;
            outline: none;
            text-align: center;
            cursor: pointer;
            transition: 0.3s;
            font-size: 17px;
            margin: 10px 0;
            border-radius: 6px;

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
                        height: 250px;
                        object-fit: cover;
                        border-radius: 4px;
                    }
                }
            }
        }

    }

    .rside {
        flex: 0 0 300px; // 固定宽度，不缩放
        padding: 0 20px 0 20px;

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
        .fruit-list ul {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media screen and (max-width: 990px) {
        .tab {
            flex: 0 0 100%;
            height: auto;
            margin-bottom: 20px;
        }

        .tab button {
            display: inline-block;
            width: auto;
            margin: 10px;
        }

        .rside {
            flex: 0 0 100%;
            padding-left: 0;
            margin-top: 20px;
        }
    }

    @media screen and (max-width: 600px) {
        .fruit-list {
            padding-left: 0;

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
    background-color: #24f563; // 与头部同色系，保持风格统一
    color: #333;
    border: none;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2); // 阴影增强层次感
    cursor: pointer;
    transition: background-color 0.3s; //  hover 过渡效果

    &:hover {
        background-color: #34ca61; //  hover 时加深颜色
    }

    i {
        font-size: 20px; // 图标大小
    }

    @media screen and (max-width: 990px) {
        display: none;
    }
}

.footer {
    background-color: #24f563;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 20px 10px;
    margin-top: 60px;
    opacity: 0.85;
    transition: opacity 0.3s ease;
    box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.08);

    &:hover {
        opacity: 1;
    }

    .footer-content {
        /* 限制最大宽度，大屏下不拉伸 */
        max-width: 1200px;
        width: 100%;
        margin: 0 auto;
        text-align: center;

        /* 地址文字样式 */
        .footer-addr {
            color: #2d3748;
            font-size: 16px;
            margin-bottom: 12px;
        }

        /* 邮箱文字样式 */
        .footer-email {
            color: #2d3748;
            font-size: 16px;
            margin-bottom: 12px;

            /* 邮箱hover时变色，增加交互感 */
            &:hover {
                color: #ffffff;
                cursor: pointer;
            }
        }

        /* 版权信息样式 */
        .footer-copyright {
            color: #4a5568;
            /* 稍浅灰色，区分主次信息 */
            font-size: 14px;
            margin-top: 5px;
        }
    }

    /* 响应式适配：小屏幕下调整文字大小和内边距 */
    @media screen and (max-width: 600px) {
        padding: 25px 10px;
        margin-top: 40px;

        .footer-content {

            .footer-addr,
            .footer-email {
                font-size: 14px;
            }

            .footer-copyright {
                font-size: 12px;
            }
        }
    }
}
</style>
