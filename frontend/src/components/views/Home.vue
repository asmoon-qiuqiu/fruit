<script setup>
import 'bootstrap-icons/font/bootstrap-icons.css'
</script>

<template>
    <div class="header">
        <a href="#">首页</a>
        <a href="#">水果种类</a>
        <a href="#">关于我们</a>
        <a href="#">联系我们</a>
        <a href="#"><i class="bi bi-box-arrow-in-right"></i>登录</a>
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
        </div>

    </div>

    <div class="footer"></div>
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
    margin: 20px 0 20px 0;
}

.header {
    background-color: #0099FF;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    border-radius: 5px;

    a {
        font-size: 18px;
        padding: 15px;
        text-decoration: none;

        .bi {
            margin-right: 5px;
        }

        &:hover,
        &:active {
            background-color: #00CCFF;
            color: #F5F9FF;
        }
    }

    @media screen and (max-width: 600px) {
        font-size: 18px;
        flex-direction: column;
        align-items: flex-start;
        padding: 10px;
        width: 100vw;
        /* 占满整个视口宽度 */
        min-width: 320px;
        /* 确保在极小屏幕上不被过度压缩 */
    }
}



.main {
    display: flex;
    flex-wrap: wrap;

    .rside {
        flex: 10%;
    }

    .tab {
        flex: 20%;
        border: 1px solid #e0f2e9;
        background-color: #f0fdf4;
        width: 30%;
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
        flex: 70%;
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
                    }

                    .fruit-img {
                        width: 100%;
                        height: 180px;
                        object-fit: cover;
                        border-radius: 4px;
                    }
                }
            }
        }
    }

    @media screen and (max-width: 990px) {
        .fruit-list ul {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media screen and (max-width: 600px) {
        .fruit-list ul {
            grid-template-columns: repeat(1, 1fr);
        }
    }
}
</style>
