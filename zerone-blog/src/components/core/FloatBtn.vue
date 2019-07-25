<template>
  <v-flex xs12 sm12 md6 offset-md3>
    <v-fab-transition>
      <v-btn v-show="btn_show" fab dark fixed bottom right color="red" @click="$vuetify.goTo(0)">
        <v-icon>keyboard_arrow_up</v-icon>
      </v-btn>
    </v-fab-transition>
  </v-flex>
</template>
<script>
export default {
  data: () => ({
    btn_show: false
  }),
  methods: {
    isShowBtn() {
      if (
        !!document.documentElement.scrollTop &&
        document.documentElement.scrollTop > 50
      ) {
        this.btn_show = true;
      } else if (document.documentElement.scrollTop == 0) {
        this.btn_show = false;
      }
    }
  },
  mounted() {
    window.addEventListener("scroll", this.isShowBtn);
  }
};
</script>
