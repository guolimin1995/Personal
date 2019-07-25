<template>
  <v-container>
    <v-layout wrap>
      <section class="animated zoomIn">
        <v-layout column wrap class="my-3" align-center>
          <v-flex xs12 sm4 class="my-3">
            <div class="text-center">
              <h2 class="headline">The best way to start developing</h2>
              <span class="subheading">Cras facilisis mi vitae nunc</span>
            </div>
          </v-flex>
          <v-flex xs12>
            <v-container grid-list-xl>
              <v-layout row wrap align-center>
                <v-flex xs12 md4 v-for="(item, i) in carInfo" :key="i">
                  <v-hover>
                    <template v-slot:default="{ hover }">
                      <v-card
                        :elevation="hover ? 0 : 8"
                        class="mx-auto transparent animated rotateIn"
                        max-width="325"
                        :loading="card_loading"
                        max-height="400"
                      >
                        <v-img
                          class="white--text imgBground"
                          height="150px"
                          aspect-ratio="1"
                          :src="`https://picsum.photos/500/300?image=${i * 5 + 10}`"
                        ></v-img>
                        <v-card-title class="white--text card-title">{{ item.title }}</v-card-title>

                        <v-card-text class="my-4">
                          <span class="text--primary">
                            <span>{{item.content.slice(0,80) + '. . . .'}}</span>
                          </span>
                        </v-card-text>

                        <v-card-actions>
                          <v-list-item class="grow">
                            <v-icon class="mr-1" color="teal darken-2">mdi-account-edit</v-icon>
                            <v-list-item-content>
                              <v-list-item-title>{{item.create_user}}</v-list-item-title>
                            </v-list-item-content>
                            <v-spacer></v-spacer>

                            <v-icon class="mr-1" color="red">mdi-heart</v-icon>
                            <span class="subheading mr-2">{{item.likes}}</span>
                            <span class="mr-1">·</span>
                            <v-icon class="mr-1" color="blue darken-2">mdi-eye</v-icon>
                            <span class="subheading">({{item.eye_view}})</span>
                          </v-list-item>
                        </v-card-actions>
                        <v-fade-transition>
                          <v-overlay v-if="hover" absolute color="grey darken-3">
                            <v-btn depressed color="grey darken-1" @click="cardMoreInfo(i)">see info</v-btn>
                          </v-overlay>
                        </v-fade-transition>
                      </v-card>
                    </template>
                  </v-hover>
                </v-flex>
              </v-layout>
            </v-container>
          </v-flex>
        </v-layout>
        <v-layout justify-center>
          <v-flex xs4 md2 lg1 sm2 class="my-4 text-center">
            <v-hover v-slot:default="{ hover }">
              <v-btn x-large :elevation="hover ? 0 : 8" outlined color="green">SEE MORE</v-btn>
            </v-hover>
          </v-flex>
        </v-layout>
        <v-layout row justify-center>
          <v-dialog v-model="card_dialog" width="800px">
            <v-card>
              <v-card-title>
                <span class="headline">{{ this.card_each_title }}</span>
              </v-card-title>
              <v-divider></v-divider>

              <v-card-text>
                <div v-html="html"></div>
              </v-card-text>
              <v-card-actions>
                <v-list-item class="grow">
                  <v-icon class="mr-1" color="teal darken-2">mdi-account-edit</v-icon>
                  <v-list-item-content>
                    <v-list-item-title>{{this.card_each_create_user}}</v-list-item-title>
                  </v-list-item-content>
                  <v-spacer></v-spacer>

                  <v-icon class="mr-1" color="red">mdi-heart</v-icon>
                  <span class="subheading mr-2">{{this.card_each_likes}}</span>
                  <span class="mr-1">·</span>
                  <v-icon class="mr-1" color="blue darken-2">mdi-eye</v-icon>
                  <span class="subheading">({{this.card_each_eye_view}})</span>
                </v-list-item>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-layout>
      </section>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    card_loading: "green",
    card_dialog: false,
    card_each_title: "",
    card_each_content: "",
    card_each_create_user: "",
    card_each_likes: "",
    card_each_eye_view: "",
    html: "",
    carInfo: [
      {
        title: "技术如何炼成，我们来一起看看",
        content:
          "于是用上了，不过还是有一些令我感到不是太友好的地方，简单在此提一下。以上。其次，同步本地评论功能，由于换了插件，所以评论都留在了本地了。同步完成之后，我并不能在畅言后台管理看到我刚才同步的评论，但是新发的评论是可以看到的，页面也是可以正常显示的。只是不能在线管理早先的原始评论了。刚在整理评论的时候吓我一跳，之前我的好多评论都没了，是的，是只有我自己的评论没有了，而其它人的评论还有。摸不着头脑的我打开多说后台管理，哦天，我之前所有的评论和回复全部自动转为垃圾评论了，八百多条啊，废了一会功夫好不容易批量还原了。结果刷新页面一看，咦，还是没有，重新刷一下后台，竟然再次把我的评论设成垃圾评论了，后来又退出重新绑定了其它平台的账号，总算还原回来了。另外，之前，多说崩溃了已经不知道多少次了。另外，多说还有一个非常令人发指的行为，会自动同步用户文章，收集用户信息，同步我们社交账号，即使是修改用户信息也要进行备份，这尼玛发展一定程度，多说还真有可能有利用这些用户信息谋利，甚至可能利用各个用户的文章做一个个性化阅读推荐也说不定。当然最开始的时候我只是觉得多说比较火，当时用上了也感觉比较方便，加上最初网站没几个东西，心想同步就同步呗，然后就一直用着了。现在再想想，也是可怕。另外，头像问题，其实我个人非常不能忍受一个账号没有头像的行为，简直是大逆不道。畅言有个QQ快速登录的功能，然而，登录之后竟然不能获取我的QQ头像！不知道是不是我这边的问题，如果大家正常希望可以反馈我一下。另外，QQ登录之后怎么会给我取了一个奇怪的用户名，叫什么cmcccc，有点醉。而微博的快速登录的昵称和头像都是正常的，然而每次评论的时候都会默认勾选那个同步到微博的按钮，这个可以默认取消么？嗯，总之换上畅言之后用起来还是比较开心的，嘿嘿主要是改好了样式，看起来一阵舒爽。嗯，换上调教好的美美的畅言还是很开心的，文章前后呼应，拜～嗯，首先我是比较追求美感的，界面问题。首先我会关注有没有个性化主题定制这个功能，畅言还是有的，支持CSS自定义。不过这个功能比较蛋疼，如果你不选择已经提供的主题，而是选择自定义CSS样式的话，你需要把所有样式重写一遍，它缺省继承了默认主题。比如我如果想在浅色主题红色风格基础上修改几个样式的话，这是办不到的，除非重写所有的红色风格样式，这就鸡肋了。建议可以选择继承某个默认主题的功能，然后自定义的CSS是在这个基础上设置的功能。而且我看WAP版本并没有自定义CSS，非常建议增加这个功能。最后我还是选择了红色主题，不过自定义样式就写在了站点全局样式表里面了，以此解决。好啦，貌似跑题了，时候不早啦，大家晚安。搜索了网上比较热门的评论插件，发现了畅言。使用了WordPress插件。昂，没错，我就是颜控！最后，有没有发表文章自动分享到各个平台的功能？我暂时没有发现。这点多说还是做得比较好的。最近博客的多说评论总是抽风，先来吐槽一下。有时候，我会因为一个屏幕膜有一点点损伤而去重新买一个新的。额，其实是因为今天给电脑贴膜折角了，我又花了几十块重新买了一个新的。有时候，我会因为一个应用的图标（没错，就是说的图标）太丑了而卸载掉，即使是它的功能再怎么好。有时候，我会因为一个样式不合我意而执着地去修改，即使要花费几个小时。有时候，我就是一个强迫症，在写上面三句话的时候，第一句原本是在第二行的，然而因为看起来长度参差不齐我就把它移动到了最上面。嗯，这第四句话要写得更长才行。果断！弃用！弃用！弃用！然后我就继续开始回复大家的评论呀，结果要发布评论的时候，点一下发布，按钮就卡在正在发布这里不动了。打开浏览器看一下Ajax出了什么问题，结果出现了一个create_json报了个500服务器错误，查看页面信息显示参数配置不正确还是怎么了，没错，是显示我的站点多说评论配置不正确。那，其它人怎么评论上来的？真是不爽的多说。还有，希望可以增加更多的平台的支持，比如微信、GitHub、脸书、推特等平台啦。",
        create_user: "zerone",
        eye_view: 4850,
        likes: 500,
        img: "../../imgs/card_img0.jpg"
      },
      {
        title: "Top 10 Australian beaches",
        content:
          "Cras facilisis mi vitae nunc lobortis pharetra. Nulla volutpat tincidunt ornare.Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.Nullam in aliquet odio. Aliquam eu est vitae tellus bibendum tincidunt. Suspendisse potenti.",
        create_user: "zerone",
        eye_view: 4850,
        likes: 500
      },
      {
        title: "Top 10 Australian beaches",
        content:
          "Cras facilisis mi vitae nunc lobortis pharetra. Nulla volutpat tincidunt ornare.Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.Nullam in aliquet odio. Aliquam eu est vitae tellus bibendum tincidunt. Suspendisse potenti.",
        create_user: "zerone",
        eye_view: 4850,
        likes: 500
      },
      {
        title: "Top 10 Australian beaches",
        content:
          "Cras facilisis mi vitae nunc lobortis pharetra. Nulla volutpat tincidunt ornare.Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.Nullam in aliquet odio. Aliquam eu est vitae tellus bibendum tincidunt. Suspendisse potenti.",
        create_user: "zerone",
        eye_view: 4850,
        likes: 500
      },
      {
        title: "Top 10 Australian beaches",
        content:
          "Cras facilisis mi vitae nunc lobortis pharetra. Nulla volutpat tincidunt ornare.Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.Nullam in aliquet odio. Aliquam eu est vitae tellus bibendum tincidunt. Suspendisse potenti.",
        create_user: "zerone",
        eye_view: 4850,
        likes: 500
      },
      {
        title: "Top 10 Australian beaches",
        content:
          "Cras facilisis mi vitae nunc lobortis pharetra. Nulla volutpat tincidunt ornare.Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.Nullam in aliquet odio. Aliquam eu est vitae tellus bibendum tincidunt. Suspendisse potenti.",
        create_user: "zerone",
        eye_view: 4850,
        likes: 500
      }
    ]
  }),
  created() {
    setTimeout(() => {
      this.card_loading = false;
    }, 2000);
    this.$vuetify.goTo(0);
  },
  methods: {
    cardMoreInfo(index) {
      console.log(index);
      this.card_each_title = this.carInfo[index].title;
      this.card_each_content = this.carInfo[index].content;
      this.card_each_create_user = this.carInfo[index].create_user;
      this.card_each_likes = this.carInfo[index].likes;
      this.card_each_eye_view = this.carInfo[index].eye_view;
      this.card_dialog = true;
    }
  }
};
</script>
<style>
/* Icon Pulse */
@-webkit-keyframes hvr-icon-pulse {
  25% {
    -webkit-transform: scale(1.3);
    transform: scale(1.3);
  }
  75% {
    -webkit-transform: scale(0.8);
    transform: scale(0.8);
  }
}
@keyframes hvr-icon-pulse {
  25% {
    -webkit-transform: scale(1.3);
    transform: scale(1.3);
  }
  75% {
    -webkit-transform: scale(0.8);
    transform: scale(0.8);
  }
}
.hvr-icon-pulse {
  display: inline-block;
  vertical-align: middle;
  -webkit-transform: perspective(1px) translateZ(0);
  transform: perspective(1px) translateZ(0);
  box-shadow: 0 0 1px rgba(0, 0, 0, 0);
}
.hvr-icon-pulse .hvr-icon {
  -webkit-transform: translateZ(0);
  transform: translateZ(0);
  -webkit-transition-timing-function: ease-out;
  transition-timing-function: ease-out;
}
.hvr-icon-pulse:hover .hvr-icon,
.hvr-icon-pulse:focus .hvr-icon,
.hvr-icon-pulse:active .hvr-icon {
  -webkit-animation-name: hvr-icon-pulse;
  animation-name: hvr-icon-pulse;
  -webkit-animation-duration: 1s;
  animation-duration: 1s;
  -webkit-animation-timing-function: linear;
  animation-timing-function: linear;
  -webkit-animation-iteration-count: infinite;
  animation-iteration-count: infinite;
}
.imgBground {
  background-attachment: fixed;
  -webkit-filter: blur(1.8px);
  -moz-filter: blur(1.8px);
  -ms-filter: blur(1.8px);
  -o-filter: blur(1.8px);
  filter: blur(1.8px);
}
.card-title {
  position: absolute;
  top: 30px;
  left: 10px;
}
</style>

