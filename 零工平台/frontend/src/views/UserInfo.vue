<template>
    <NavBar />
</template>

<script>
import NavBar from '@/components/NavBar.vue';
import { useRoute } from 'vue-router';
import $ from 'jquery';
import { ref } from 'vue';

export default {
    name: 'UserInfo',
    components: {
        NavBar,
    },
    setup() {
        const route = useRoute();
        const username = route.params.username;
        let userinfo = ref({});

        $.ajax({
            url: 'http://127.0.0.1:8000/api/getotherinfo/',
            data: {
                username: username,
            },
            success: response => {
                console.log(response, userinfo);
            }
        })
    }
}
</script>

<style scoped></style>