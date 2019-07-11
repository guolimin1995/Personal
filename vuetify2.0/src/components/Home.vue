<template>
  <v-app>
    <section class="animated bounceIn">
      <v-parallax src="../imgs/back1.png" width="100%" height="600">
        <v-container>
          <v-layout justify-center>
            <v-flex xs12 md12 lg12 text-xs-center>
              <div class="text-xs-center animated bounceInDown">
                <v-btn class="my-4 title hvr-grow-shadow" text color="white">HOME</v-btn>
                <v-btn class="my-4 title hvr-grow-shadow" text color="white">DATEFILE</v-btn>
                <v-btn class="my-4 title hvr-grow-shadow" text color="white">ABOUT</v-btn>
              </div>
              <v-avatar size="150" class="my-5 animated jackInTheBox">
                <img src="../imgs/back.jpeg" class="mx-auto hvr-grow-shadow" alt="avatar" />
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
                  <v-card class="mx-auto transparent animated rotateIn" :elevation="hover ? 0 : 10">
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
            <v-btn color="pink" absolute bottom right fab>
              <v-icon>⤴️</v-icon>
            </v-btn>
          </v-container>
        </v-flex>
      </v-layout>
    </section>
  </v-app>
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
.hvr-grow-shadow {
  display: inline-block;
  vertical-align: middle;
  -webkit-transform: perspective(1px) translateZ(0);
  transform: perspective(1px) translateZ(0);
  box-shadow: 0 0 1px rgba(0, 0, 0, 0);
  -webkit-transition-duration: 0.3s;
  transition-duration: 0.3s;
  -webkit-transition-property: box-shadow, transform;
  transition-property: box-shadow, transform;
}
.hvr-grow-shadow:hover,
.hvr-grow-shadow:focus,
.hvr-grow-shadow:active {
  box-shadow: 0 10px 10px -10px rgba(0, 0, 0, 0.5);
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>

