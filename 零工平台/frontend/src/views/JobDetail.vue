<template>
    <NavBar />
    <div class="job-banner">销售顾问</div>
    <ContentBase>
        <b>职位描述</b>
        {{ }}
    </ContentBase>
</template>

<script>
import NavBar from '@/components/NavBar.vue';
import { useRoute } from 'vue-router';
import ContentBase from '@/components/ContentBase.vue';
import $ from 'jquery';
import { ref } from 'vue';

export default {
    name: 'JobDetail',
    components: {
        NavBar,
        ContentBase,
    },
    setup() {
        const route = useRoute();
        const jobid = route.params.jobid;
        let job = ref({});

        $.ajax({
            url: 'http://127.0.0.1:8000/api/jobs',
            type: 'GET',
            data: {
                jobid: jobid,
            },
            success: response => {
                job.value = response;
            }
        })
        console.log(job);
        return {
            job,
        }
    }
}
</script>

<style scoped></style>