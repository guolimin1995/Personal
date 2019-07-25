<template>
  <v-footer>
    <v-card flat tile class="blue-grey lighten-2 white--text text-center" width="100%">
      <v-card-text class="white--text pt-2">this is footer.</v-card-text>

      <v-divider></v-divider>

      <v-card-text class="white--text">
        {{ new Date().getFullYear() }} —
        <strong>Powered by Zerone</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>