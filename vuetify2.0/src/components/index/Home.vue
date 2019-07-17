<template>
  <v-container>
    <v-layout wrap>
      <v-content>
        <section class="animated bounceIn">
          <v-parallax src="../../imgs/back2_2.png" width="100%" height="600">
            <v-container>
              <v-layout justify-center>
                <v-flex xs12 md12 lg12 text-xs-center>
                  <!-- <div class="text-xs-center animated bounceInDown">
                <v-btn class="my-4 title hvr-grow-shadow" text color="white">HOME</v-btn>
                <v-btn class="my-4 title hvr-grow-shadow" text color="white">DATEFILE</v-btn>
                <v-btn class="my-4 title hvr-grow-shadow" text color="white">ABOUT</v-btn>
                  </div>-->
                  <v-avatar size="150" class="my-5 animated jackInTheBox hvr-icon-pulse">
                    <img src="../../imgs/back.jpeg" class="hvr-icon" alt="avatar" />
                  </v-avatar>

                  <h1 class="white--text mb-2 display-1 text-xs-center">Personal Blog</h1>
                  <div class="subheading mb-3 text-xs-center">Powered by Zerone</div>
                </v-flex>
              </v-layout>
            </v-container>
          </v-parallax>
        </section>
        <section class="animated zoomIn">
          <v-layout column wrap class="my-5" align-center>
            <v-flex xs12 sm4 class="my-3">
              <div class="text-xs-center">
                <h2 class="headline">The best way to start developing</h2>
                <span class="subheading">Cras facilisis mi vitae nunc</span>
              </div>
            </v-flex>
            <v-flex xs12>
              <v-container grid-list-xl>
                <v-layout row wrap align-center>
                  <v-flex xs12 md4>
                    <v-hover v-slot:default="{ hover }">
                      <v-card
                        class="mx-auto transparent animated rotateIn"
                        :elevation="hover ? 0 : 10"
                      >
                        <v-card-text class="text-xs-center">
                          <v-icon x-large class="blue--text text--lighten-2">color_lens</v-icon>
                        </v-card-text>
                        <v-card-title primary-title class="layout justify-center">
                          <div class="headline text-xs-center">Material Design</div>
                        </v-card-title>
                        <v-card-text>
                          Cras facilisis mi vitae nunc lobortis pharetra. Nulla volutpat tincidunt ornare.
                          Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.
                          Nullam in aliquet odio. Aliquam eu est vitae tellus bibendum tincidunt. Suspendisse potenti.
                        </v-card-text>
                      </v-card>
                    </v-hover>
                  </v-flex>
                  <v-flex xs12 md4>
                    <v-card class="elevation-0 transparent animated rotateIn">
                      <v-card-text class="text-xs-center">
                        <v-icon x-large class="blue--text text--lighten-2">flash_on</v-icon>
                      </v-card-text>
                      <v-card-title primary-title class="layout justify-center">
                        <div class="headline">Fast development</div>
                      </v-card-title>
                      <v-card-text>
                        Cras facilisis mi vitae nunc lobortis pharetra. Nulla volutpat tincidunt ornare.
                        Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.
                        Nullam in aliquet odio. Aliquam eu est vitae tellus bibendum tincidunt. Suspendisse potenti.
                      </v-card-text>
                    </v-card>
                  </v-flex>
                  <v-flex xs12 md4>
                    <v-card class="elevation-0 transparent animated rotateIn">
                      <v-card-text class="text-xs-center">
                        <v-icon x-large class="blue--text text--lighten-2">build</v-icon>
                      </v-card-text>
                      <v-card-title primary-title class="layout justify-center">
                        <div class="headline text-xs-center">Completely Open Sourced</div>
                      </v-card-title>
                      <v-card-text>
                        Cras facilisis mi vitae nunc lobortis pharetra. Nulla volutpat tincidunt ornare.
                        Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.
                        Nullam in aliquet odio. Aliquam eu est vitae tellus bibendum tincidunt. Suspendisse potenti.
                      </v-card-text>
                    </v-card>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-flex>
          </v-layout>
        </section>
        <section class="animated zoomIn">
          <v-layout column wrap class="my-5" align-center>
            <v-flex xs12 sm4 class="my-3">
              <div class="text-xs-center">
                <h2 class="headline">The best way to start developing</h2>
                <span class="subheading">Cras facilisis mi vitae nunc</span>
              </div>
            </v-flex>
            <v-flex xs12>
              <v-container grid-list-xl>
                <v-layout row wrap align-center>
                  <v-flex xs12 md4>
                    <v-hover v-slot:default="{ hover }">
                      <v-card
                        class="mx-auto transparent animated rotateIn"
                        :elevation="hover ? 0 : 10"
                      >
                        <v-card-text class="text-xs-center">
                          <v-icon x-large class="blue--text text--lighten-2">color_lens</v-icon>
                        </v-card-text>
                        <v-card-title primary-title class="layout justify-center">
                          <div class="headline text-xs-center">Material Design</div>
                        </v-card-title>
                        <v-card-text>
                          Cras facilisis mi vitae nunc lobortis pharetra. Nulla volutpat tincidunt ornare.
                          Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.
                          Nullam in aliquet odio. Aliquam eu est vitae tellus bibendum tincidunt. Suspendisse potenti.
                        </v-card-text>
                      </v-card>
                    </v-hover>
                  </v-flex>
                  <v-flex xs12 md4>
                    <v-card class="elevation-0 transparent animated rotateIn">
                      <v-card-text class="text-xs-center">
                        <v-icon x-large class="blue--text text--lighten-2">flash_on</v-icon>
                      </v-card-text>
                      <v-card-title primary-title class="layout justify-center">
                        <div class="headline">Fast development</div>
                      </v-card-title>
                      <v-card-text>
                        Cras facilisis mi vitae nunc lobortis pharetra. Nulla volutpat tincidunt ornare.
                        Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.
                        Nullam in aliquet odio. Aliquam eu est vitae tellus bibendum tincidunt. Suspendisse potenti.
                      </v-card-text>
                    </v-card>
                  </v-flex>
                  <v-flex xs12 md4>
                    <v-card class="elevation-0 transparent animated rotateIn">
                      <v-card-text class="text-xs-center">
                        <v-icon x-large class="blue--text text--lighten-2">build</v-icon>
                      </v-card-text>
                      <v-card-title primary-title class="layout justify-center">
                        <div class="headline text-xs-center">Completely Open Sourced</div>
                      </v-card-title>
                      <v-card-text>
                        Cras facilisis mi vitae nunc lobortis pharetra. Nulla volutpat tincidunt ornare.
                        Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.
                        Nullam in aliquet odio. Aliquam eu est vitae tellus bibendum tincidunt. Suspendisse potenti.
                      </v-card-text>
                    </v-card>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-flex>
          </v-layout>
        </section>
        <section class="animated zoomIn">
          <v-layout column wrap class="my-5" align-center>
            <v-flex xs12 sm4 class="my-3">
              <div class="text-xs-center">
                <h2 class="headline">The best way to start developing</h2>
                <span class="subheading">Cras facilisis mi vitae nunc</span>
              </div>
            </v-flex>
            <v-flex xs12>
              <v-container grid-list-xl>
                <v-layout row wrap align-center>
                  <v-flex xs12 md4>
                    <v-hover v-slot:default="{ hover }">
                      <v-card
                        class="mx-auto transparent animated rotateIn"
                        :elevation="hover ? 0 : 10"
                      >
                        <v-card-text class="text-xs-center">
                          <v-icon x-large class="blue--text text--lighten-2">color_lens</v-icon>
                        </v-card-text>
                        <v-card-title primary-title class="layout justify-center">
                          <div class="headline text-xs-center">Material Design</div>
                        </v-card-title>
                        <v-card-text>
                          Cras facilisis mi vitae nunc lobortis pharetra. Nulla volutpat tincidunt ornare.
                          Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.
                          Nullam in aliquet odio. Aliquam eu est vitae tellus bibendum tincidunt. Suspendisse potenti.
                        </v-card-text>
                      </v-card>
                    </v-hover>
                  </v-flex>
                  <v-flex xs12 md4>
                    <v-card class="elevation-0 transparent animated rotateIn">
                      <v-card-text class="text-xs-center">
                        <v-icon x-large class="blue--text text--lighten-2">flash_on</v-icon>
                      </v-card-text>
                      <v-card-title primary-title class="layout justify-center">
                        <div class="headline">Fast development</div>
                      </v-card-title>
                      <v-card-text>
                        Cras facilisis mi vitae nunc lobortis pharetra. Nulla volutpat tincidunt ornare.
                        Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.
                        Nullam in aliquet odio. Aliquam eu est vitae tellus bibendum tincidunt. Suspendisse potenti.
                      </v-card-text>
                    </v-card>
                  </v-flex>
                  <v-flex xs12 md4>
                    <v-card class="elevation-0 transparent animated rotateIn">
                      <v-card-text class="text-xs-center">
                        <v-icon x-large class="blue--text text--lighten-2">build</v-icon>
                      </v-card-text>
                      <v-card-title primary-title class="layout justify-center">
                        <div class="headline text-xs-center">Completely Open Sourced</div>
                      </v-card-title>
                      <v-card-text>
                        Cras facilisis mi vitae nunc lobortis pharetra. Nulla volutpat tincidunt ornare.
                        Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.
                        Nullam in aliquet odio. Aliquam eu est vitae tellus bibendum tincidunt. Suspendisse potenti.
                      </v-card-text>
                    </v-card>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-flex>
          </v-layout>
        </section>
      </v-content>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data: () => ({})
};
</script>
<style>
.parallaxs {
  background-attachment: fixed;
  -webkit-filter: blur(20px);
  -moz-filter: blur(20px);
  -ms-filter: blur(20px);
  -o-filter: blur(20px);
  filter: blur(10px);
}
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
</style>

