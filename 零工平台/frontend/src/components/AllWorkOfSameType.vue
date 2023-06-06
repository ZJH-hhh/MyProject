<template>
    <div class="card" v-for="job in jobs" :key="job.id" @click="search(job.name)">
        <div class="card-body">{{ job.name }}</div>
    </div>
</template>

<script>
import $ from 'jquery';
import { useRouter } from 'vue-router';

export default {
    name: 'AllWorkOfSameType',
    props: {
        jobs: {
            type: Object,
            required: true,
        }
    },
    setup() {
        const router = useRouter();

        const search = jobname => {
            $.ajax({
                url: 'http://127.0.0.1:8000/api/jobs/',
                type: 'GET',
                data: {
                    'jobname': jobname,
                },
                success: () => {
                    // console.log(response);
                    router.push({ name: 'jobs', params: { 'jobname': jobname } });
                }
            });
        }

        return {
            search,
        }
    }
}
</script>

<style scoped>
.card {
    cursor: pointer;
}
</style>