<script setup>
import Footer from '@/components/Footer.vue';
import Header from '@/components/Header.vue';
</script>
<template>
    <Header></Header>
    <div class="login">
        <form class="login-form" action="#" method="get">
            <h3>账户登录</h3>
            <p>请输入您的账户信息</p>
            <!-- 用户名输入 -->
            <div class="login-name">
                <input type="text" name="username" placeholder="用户名/邮箱" required>
            </div>

            <!-- 密码输入 -->
            <div class="login-password">
                <input type="password" name="pwd" placeholder="密码" required>
                <i class="bi bi-eye"></i>
            </div>

            <div class="login-button">
                <input type="submit" value="登录">
            </div>
        </form>
    </div>

    <div class="clearfix">

    </div>
    <Footer></Footer>
</template>


<style scoped lang="scss">
.login {
    position: relative;
    // 假设头部+底部总高约150px，可根据实际调整
    min-height: calc(100vh - 150px);
    position: relative;
    padding: 20px; // 避免表单贴边

    &-form {
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        max-width: 350px; // 限制表单宽度，避免过宽
        width: 100%; // 响应式宽度
        background-color: #f5f7fa;
        padding: 30px;
        border-radius: 8px; // 可选，增加圆角
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); // 可选，增加阴影

    }
}


.clearfix::after {
    content: "";
    clear: both;
    display: table;
}
</style>