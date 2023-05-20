<template>
    <NavBar />
    <SearchWork />
    <div class="platform-home">
        <IntroduceWork />
    </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue';
import SearchWork from '@/components/SearchWork.vue'
import IntroduceWork from '../components/IntroduceWork.vue'

export default {
    name: 'HomeView',
    components: {
        IntroduceWork,
        NavBar,
        SearchWork,
    }
}
</script>

<style scoped>
.platform-home {
    height: 100vh;
    background-color: #E4F3F5;
}
</style>