<script setup></script>

<template>
  <div class="about">
    <div class="about-content">
      <h3>此站说明</h3>
      <div class="about-explanation">
        <p>
          此站为个人
          <span class="user">
            (asmoon)
            <i class="bi bi-emoji-smile"></i>
          </span>
          独自开发维护的项目，旨在为用户提供第一时间的水果资讯和优质的水果购买体验。希望你们能够喜欢这个网站，并提供宝贵的反馈意见，让我们一起把它做得更好！
          <img
            class="manbo"
            src="../../public/images/manbo2.gif"
            alt="曼波"
          />
        </p>
        <p>此外,此网站已在GitHub开源，欢迎大家前往查看代码，提出建议或贡献代码。</p>
        <p>祝大家预览愉快！</p>
      </div>

      <div class="about-github">
        <h3>链接如下：</h3>
        <a
          href="https://github.com/asmoon-qiuqiu"
          class="github-link"
          target="_blank"
        >
          <p>GitHub：https://github.com/asmoon-qiuqiu</p>
        </a>
        <a
          href="https://github.com/asmoon-qiuqiu/FruitSync"
          class="github-link"
          target="_blank"
        >
          <p>项目仓库:https://github.com/asmoon-qiuqiu/FruitSync</p>
        </a>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
  $primary-color: #fff0f5; // 主题颜色变量
  $minor-color: #c2185b;

  .about {
    min-height: calc(100vh - 176px);
    background: url(../../public/images/about.jpg) no-repeat center;
    background-size: cover;
    background-attachment: fixed;
    padding: 10px;
    position: relative;

    .about-content {
      background: rgba(255, 240, 245, 0.3);
      position: absolute;
      width: 80%;
      padding: 10px;
      left: 0;
      right: 0;
      margin: 0 auto;
      top: 50%;
      transform: translateY(-50%);

      h3,
      h4 {
        margin-top: 10px;
        color: $minor-color;
      }

      .about-explanation {
        .user {
          color: $primary-color;
          font-weight: bold;
        }

        .manbo {
          float: right;
          border: 1px solid #b0938d;
          border-radius: 50px;
          width: 100px;
          height: 100px;
          margin-right: 10px;
        }
      }

      .about-github {
        .github-link {
          color: $minor-color;
          font-size: 18px;
          text-decoration: none;

          &:hover {
            color: #8d6e63;
          }
        }
      }
    }
  }
</style>
