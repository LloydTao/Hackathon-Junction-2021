<template>
  <div class="bg-blue-700">
    <nav class="flex container mx-auto px-5 py-5">
      <ul class="flex flex-grow space-x-4">
        <li>
          <a href="/" class="flex items-center space-x-3 text-gray-700 md:mr-5">
            <img class="flex w-10 h-10" src="~/assets/Component-1.svg" />
            <span class="text-gray-50 hover:text-gray-300 text-xl py-1">
              <span class="font-semibold">KeepChat </span>Admin</span
            >
          </a>
        </li>
      </ul>
      <ul class="flex items-center space-x-5">
        <li class="hidden sm:flex">
          <a
            href="/"
            class="
              text-gray-50
              hover:text-gray-400
              text-lg
              font-semibold
              py-1
              px-3
            "
            >Home</a
          >
        </li>
        <li class="hidden sm:flex">
          <a
            href="/users"
            class="
              text-gray-50
              hover:text-gray-400
              text-lg
              font-semibold
              py-1
              px-3
            "
            >Users</a
          >
        </li>
        <li class="hidden sm:flex">
          <a
            href="/rooms"
            class="
              text-gray-50
              hover:text-gray-400
              text-lg
              font-semibold
              py-1
              px-3
            "
            >Rooms</a
          >
        </li>
      </ul>
      <ul class="flex sm:hidden" @click="showMenu = !showMenu">
        <li>
          <a href="#" class="flex-none absolute right-0 px-5 z-30">
            <p
              class="
                text-gray-200
                font-semibold
                tracking-wide
                hover:bg-gray-900 hover:bg-opacity-30
                rounded
                px-2
                py-2
              "
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                class="h-6 w-6"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M4 6h16M4 12h16m-7 6h7"
                ></path>
              </svg>
            </p>
          </a>
          <div
            class="
              absolute
              top-0
              right-0
              z-10
              h-screen
              w-full
              bg-black
              transition
            "
            :class="{
              'invisible opacity-0': !showMenu,
              'visible opacity-40': showMenu,
            }"
          ></div>
          <div
            class="absolute right-0 z-20 w-full px-5 mt-20 transition"
            :class="{
              'invisible opacity-0': !showMenu,
              'visible opacity-100': showMenu,
            }"
          >
            <ul
              class="
                flex flex-col
                bg-gray-100
                w-full
                rounded
                shadow-md
                overflow-hidden
              "
            >
              <li class="flex">
                <h3 class="flex flex-1 text-gray-600 font-semibold px-5 py-4">
                  Navigation
                </h3>
              </li>
              <li class="flex border-t">
                <a
                  href="/"
                  class="
                    flex flex-1
                    text-lg text-gray-700
                    hover:bg-gray-200
                    font-semibold
                    px-8
                    py-4
                  "
                  >Home</a
                >
              </li>
              <li class="flex">
                <a
                  href="/users"
                  class="
                    flex flex-1
                    text-lg text-gray-700
                    hover:bg-gray-200
                    font-semibold
                    px-8
                    py-4
                  "
                  >Users</a
                >
              </li>
              <li class="flex">
                <a
                  href="/rooms"
                  class="
                    flex flex-1
                    text-lg text-gray-700
                    hover:bg-gray-200
                    font-semibold
                    px-8
                    py-4
                  "
                  >Rooms</a
                >
              </li>
            </ul>
          </div>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showMenu: false,
    }
  },
}
</script>

<style></style>
