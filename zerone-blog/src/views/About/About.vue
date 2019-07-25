<template>
  <v-container>
    <v-layout justify-center wrap>
      <v-flex xs12 md10 lg8 class="my-4">
        <v-hover>
          <template v-slot:default="{ hover }">
            <v-card :elevation="hover ? 0 : 8" flat class="transparent animated rotateIn">
              <v-img
                class="white--text"
                height="300px"
                src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
              >
                <v-card-title class="align-end fill-height">MY INFO</v-card-title>
              </v-img>
              <v-card-title>
                <span class="title font-weight-bold">WORK INFO</span>
              </v-card-title>
              <v-divider></v-divider>
              <v-card-text
                class="headline"
              >Turns out semicolon-less style is easier and safer in TS because most gotcha edge cases are type invalid as well</v-card-text>
              <v-card-title>
                <span class="title font-weight-bold">Skills and Expertize</span>
              </v-card-title>
              <v-divider></v-divider>
              <v-layout wrap class="my-3">
                <template v-for="(skill, i) in skills">
                  <v-flex v-if="skill.divider" :key="i" md12 xs12 mb-4 />
                  <v-flex v-else :key="i" md6 xs12>
                    <div class="mr-2 ml-2">
                      <div class="align-center">
                        <v-icon small>{{ skill.icon }}</v-icon>
                        {{ skill.title }}
                      </div>
                      <v-progress-linear
                        class="progress"
                        color="secondary"
                        height="6"
                        :value="skill.value"
                        striped
                      />
                    </div>
                  </v-flex>
                </template>
              </v-layout>
              <v-card-title>
                <span class="title font-weight-bold">CONTENCTS ME</span>
              </v-card-title>
              <v-divider></v-divider>
              <v-layout class="my-3">
                <v-flex md12 xs12 class="ml-3">
                  <v-icon>mdi-email</v-icon>
                </v-flex>
                <v-flex md12 xs12>
                  <div class>Email</div>
                </v-flex>
                <v-flex md12 xs12>
                  <span class="grey--text">913108060@qq.com</span>
                </v-flex>
              </v-layout>
              <v-layout class="my-3">
                <v-flex md12 xs12 class="ml-3">
                  <v-icon>mdi-web</v-icon>
                </v-flex>
                <v-flex md12 xs12>
                  <div>Website</div>
                </v-flex>
                <v-flex md12 xs12>
                  <span class="grey--text">baidu.com</span>
                </v-flex>
              </v-layout>
              <v-layout class="my-3">
                <v-flex md12 xs12 class="ml-3">
                  <v-icon>mdi-map-marker</v-icon>
                </v-flex>
                <v-flex md12 xs12>
                  <div>Location</div>
                </v-flex>
                <v-flex md12 xs12>
                  <span class="grey--text">GuangZhou.China</span>
                </v-flex>
              </v-layout>
            </v-card>
          </template>
        </v-hover>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: "About",
  data: () => ({
    skills: [
      {
        title: "Python",
        icon: "mdi-language-python",
        value: 76
      },
      {
        title: "Go",
        icon: "mdi-language-go",
        value: 65
      },
      {
        title: "PHP",
        icon: "mdi-language-php",
        value: 72
      },
      {
        title: "JavaScript",
        icon: "mdi-language-javascript",
        value: 68
      },
      {
        title: "Html + Css",
        icon: "mdi-language-html5",
        value: 68
      },
      {
        title: "Vue.js Framework(vuetifyjs iView)",
        icon: "mdi-vuejs",
        value: 70
      },
      { divider: true },
      {
        title: "Ubuntu CentOS Mac Servers",
        icon: "mdi-linux",
        value: 70
      },
      {
        title: "Git",
        icon: "mdi-git",
        value: 67
      },
      {
        title: "Database(mysql postgresql redis)",
        icon: "mdi-database",
        value: 70
      },
      { divider: true },
      {
        title: "Laravel Framework",
        icon: "mdi-laravel",
        value: 68
      },
      {
        title: "Django Framework",
        icon: "mdi-alpha-d-box",
        value: 75
      },
      {
        title: "Go Framework (Beego Iris)",
        icon: "mdi-language-go",
        value: 60
      }
    ]
  }),
  created() {
    this.$vuetify.goTo(0);
  }
};
</script>
<style>
</style>