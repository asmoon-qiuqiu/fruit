<template>
    <div class="footer">
        <div class="footer-content">
            <p class="footer-addr">地址: 广东省惠州市惠东县黄埠镇</p>
            <p class="footer-email">联系邮箱: 2371824615@qq.com</p>
            <p class="footer-copyright">© 2025 个人制作 版权所有</p>
        </div>
    </div>
</template>


<style scoped lang="scss">
.footer {
    background-color: #24f563;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 20px 10px;
    margin-top: 15px;
    opacity: 0.85;
    transition: opacity 0.3s ease;
    box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.08);

    &:hover {
        opacity: 1;
    }

    .footer-content {
        /* 限制最大宽度，大屏下不拉伸 */
        max-width: 1200px;
        margin: 0 auto;
        text-align: center;

        /* 地址文字样式 */
        .footer-addr {
            color: #2d3748;
            font-size: 16px;
            margin-bottom: 10px;
        }

        /* 邮箱文字样式 */
        .footer-email {
            color: #2d3748;
            font-size: 16px;
            margin-bottom: 10px;

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
            margin-bottom: -10px;
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