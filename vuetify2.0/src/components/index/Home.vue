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
                      >
                        <v-img
                          class="white--text imgBground"
                          height="150px"
                          src="https://picsum.photos/1920/1080?random"
                        ></v-img>
                        <v-card-title class="card-title">{{ item.title }}</v-card-title>

                        <v-card-text>
                          <span class="text--primary">
                            <span>{{item.content}}</span>
                          </span>
                        </v-card-text>

                        <v-card-actions>
                          <v-list-item class="grow">
                            <v-icon class="mr-1">mdi-account-edit</v-icon>
                            <v-list-item-content>
                              <v-list-item-title>{{item.create_user}}</v-list-item-title>
                            </v-list-item-content>
                            <v-spacer></v-spacer>

                            <v-icon class="mr-1">mdi-heart</v-icon>
                            <span class="subheading mr-2">{{item.likes}}</span>
                            <span class="mr-1">·</span>
                            <v-icon class="mr-1">mdi-eye</v-icon>
                            <span class="subheading">({{item.eye_view}})</span>
                          </v-list-item>
                        </v-card-actions>
                        <v-fade-transition>
                          <v-overlay v-if="hover" absolute color="grey darken-3">
                            <v-btn depressed color="grey darken-1">see info</v-btn>
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
      </section>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    carInfo: [
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
  })
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
  top: 15%;
  left: 10%;
}
</style>

