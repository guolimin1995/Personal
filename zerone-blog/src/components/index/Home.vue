<template>
  <v-container>
    <v-layout wrap>
      <section class="animated zoomIn">
        <v-layout column wrap class="my-3" align-center>
          <v-flex xs12 sm4 class="my-3">
            <div class="text-xs-center">
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
                            <span>{{item.content.slice(0,150) + '. . . .'}}</span>
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
          <v-flex xs4 md2 lg1 sm2 class="my-4">
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
              <v-card-text>{{ this.card_each_content }}</v-card-text>
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
    carInfo: [
      {
        title: "技术如何炼成，我们来一起看看",
        content:
          "技术如何炼成 Cras facilisis mi vitae nunc lobortis pharetra. </br> Nulla volutpat tincidunt ornare.Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.Nullam in aliquet odio. Aliquam eu est vitae tellus bibendum tincidunt. Suspendisse potenti.",
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
  -webkit-filter: blur(1.5px);
  -moz-filter: blur(1.5px);
  -ms-filter: blur(1.5px);
  -o-filter: blur(1.5px);
  filter: blur(1.5px);
}
.card-title {
  position: absolute;
  top: 30px;
  left: 10px;
}
</style>

