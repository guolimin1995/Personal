<template>
  <v-navigation-drawer v-model="drawer" app dark src="../../imgs/toolbar.png" width="60%" temporary>
    <v-list>
      <v-list-item v-for="([icon, text, to], i) in items" :key="i">
        <v-list-item-icon>
          <v-icon>{{ icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title @click="onClick($event, to)">{{ text }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>
<script>
// Utilities
import { mapMutations } from "vuex";

export default {
  name: "CoreDrawer",
  data: () => ({
    items: [
      ["mdi-email", "DATEFILE", "/article"],
      ["mdi-account-supervisor-circle", "ABOUT", "/about"],
      ["mdi-clock-start", "CONTECTS", "/"]
    ]
  }),

  computed: {
    drawer: {
      get() {
        return this.$store.state.drawer;
      },
      set(val) {
        this.setDrawer(val);
      }
    }
  },

  methods: {
    ...mapMutations(["setDrawer"]),
    onClick(e, to) {
      e.stopPropagation();
      let redirect = decodeURIComponent(this.$route.query.redirect || to);
      this.$router.push({ path: redirect });
      this.setDrawer(false);
    }
  }
};
</script>