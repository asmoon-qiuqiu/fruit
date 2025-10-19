<template>
    <div class="header">
        <router-link to="/">首页</router-link>
        <a href="#">水果种类</a>
        <a href="#">关于我们</a>
        <a href="#">联系我们</a>
        <router-link to="login">
            <i class="bi bi-box-arrow-in-right"></i>登录
        </router-link>
    </div>
</template>

<style scoped lang="scss">
.header {
    background-color: #24f563;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    border-radius: 5px;

    & :last-child {
        font-style: italic;
    }

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
</style>