<template>
  <v-app>
    <core-toolbar />
    <core-drawer />
    <core-view />
    <core-floatBtn />
    <core-footer />
  </v-app>
</template>

<script>
export default {
  name: "App",
  components: {
    CoreToolbar: () => import("@/components/core/Toolbar"),
    CoreView: () => import("@/components/core/View"),
    CoreFloatBtn: () => import("@/components/core/FloatBtn"),
    CoreFooter: () => import("@/components/core/Footer"),
    CoreDrawer: () => import("@/components/core/Drawer")
  },
  data: () => ({}),
  created() {}
};
</script>
<style>
</style>

