<template>
  <div class="min-h-screen bg-image">
    <Navbar />
    <Nuxt />
    <Footer />
  </div>
</template>

<style>
.bg-image {
  background: rgb(231, 231, 231);
  background: linear-gradient(
    90deg,
    rgba(231, 231, 231, 1) 0%,
    rgba(196, 205, 255, 1) 100%
  );
}
</style>
