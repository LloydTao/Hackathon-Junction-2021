<template>
  <section class="container mx-auto">
    <div class="w-full rounded-lg">
      <div class="w-full overflow-x-auto">
        <h1 class="text-xl text-gray-900 font-semibold mt-3">Dashboard</h1>
        <DashboardCards />
        <h1 class="text-xl text-gray-900 font-semibold mt-8">Default chat</h1>
        <DashboardChat />
      </div>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      user: {
        id: 1,
        username: 'lloydtao',
        role: 'Player',
        created: '2021-11-16',
        rating: 1000,
        status: 1,
      },
    }
  },
}
</script>
