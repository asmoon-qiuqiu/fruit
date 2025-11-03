<script setup>
import { ref } from 'vue';
// 响应式变量：控制菜单显示/隐藏
const isMenuOpen = ref(false); // 抽屉是否打开-默认关闭
const isMenuVisible = ref(false);

// 菜单和关闭按钮逻辑
const toggleMenu = () => {
    isMenuOpen.value = !isMenuOpen.value;
    if (isMenuOpen.value) {
        // 打开时显示元素
        isMenuVisible.value = true;
    } else {
        // 关闭时，等动画结束（300ms 对应动画时长）再隐藏
        setTimeout(() => {
            isMenuVisible.value = false;
        }, 300);
    }
};

</script>
<template>
    <!-- 1. 小屏幕触发按钮（仅在≤600px显示） -->
    <div class="mini-header">
        <router-link to="/">
            <i class="bi bi-house"></i>
        </router-link>
        <!-- 抽屉菜单按钮 -->
        <button class="menu-btn" @click="toggleMenu" v-show="!isMenuOpen">
            <i class="bi bi-list"></i>
        </button>

        <!-- 抽屉关闭按钮 -->
        <button class="close-btn" @click="toggleMenu" v-show="isMenuOpen">
            <i class="bi bi-x"></i>
        </button>

        <!-- 2. 小屏幕侧边抽屉（从右侧弹出，≤600px显示） -->
        <div class="mobile-menu" :class="{ 'open': isMenuOpen, 'close': !isMenuOpen }" v-show="isMenuVisible">
            <!-- 抽屉菜单内容 -->
            <div class="menu-content">
                <router-link to="/">首页</router-link>
                <a href="#">水果种类</a>
                <a href="#">关于我们</a>
                <a href="#">联系我们</a>
                <router-link to="login">
                    <i class="bi bi-box-arrow-in-right"></i>登录
                </router-link>
            </div>
        </div>
    </div>

    <!-- 3. 大屏幕导航（原导航，≥601px显示） -->
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
    background-color: #FFF0F5;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    border-radius: 5px;

    & :last-child {
        font-style: italic;
    }

    a {
        font-size: 18px;
        padding: 15px;
        text-decoration: none;
        color: #C2185B;

        .bi {
            margin-right: 5px;
        }

        &:hover,
        &:active {
            background-color: #C2185B;
            color: #F5F9FF;
        }
    }
}

@media screen and (max-width: 600px) {
    .header {
        display: none;
    }

    .bi-house {
        color: #C2185B;
        font-size: 24px;
        text-align: center;
    }

    .mini-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: relative; // 为侧边抽屉做定位参考
        background-color: #fff0f5;

        // 菜单按钮样式
        .menu-btn {
            z-index: 999;
            border: none;
            font-size: 24px;
            color: #FFF0F5;
            background-color: #C2185B;
            padding: 5px;
            cursor: pointer;
        }

        // 关闭按钮样式
        .close-btn {
            z-index: 999;
            border: none;
            font-size: 24px;
            color: #333;
            background-color: #fff0f5;
            padding: 5px;
            cursor: pointer;
        }

        // 打开菜单动画
        @keyframes openMenu {
            from {
                transform: translateX(100%); //初始状态：完全在右侧外部 
            }

            to {
                transform: translateX(0); //结束状态：滑入到正常位置 
            }
        }

        @keyframes closeMenu {
            from {
                transform: translateX(0); //初始状态：完全在右侧外部 
            }

            to {
                transform: translateX(100%); //结束状态：滑入到正常位置 
            }
        }

        // 侧边抽屉
        .mobile-menu {
            position: absolute;
            width: 200px;
            height: 100vh;
            z-index: 998;
            top: 0;
            right: 0; // 从右侧弹出
            background-color: #FFF0F5;
            box-shadow: -20px 0 10px rgba(0, 0, 0, 0.1);
            //滑出动画
            animation-duration: 0.3s;
            animation-timing-function: ease;
            animation-iteration-count: 1;
            animation-fill-mode: forwards;
            transform: translateX(100%);

            &.open {
                animation-name: openMenu;
                // 打开后允许点击
                pointer-events: auto;
            }

            &.close {
                animation-name: closeMenu;
                // 关闭后禁止点击（可选）
                pointer-events: none;
            }

            // 抽屉菜单内容
            .menu-content {
                display: flex;
                flex-direction: column;
                padding: 50px 30px 0 0;


                a {
                    font-size: 18px;
                    padding: 15px;
                    text-decoration: none;
                    color: #C2185B;
                }

                a:hover,
                a:active {
                    background-color: #C2185B;
                    color: white;
                }
            }
        }
    }

    a {

        &:hover,
        &:active {
            color: white;
        }
    }


}

// 大屏幕隐藏小屏幕菜单容器
@media screen and (min-width: 601px) {
    .mini-header {
        display: none;
    }
}
</style>