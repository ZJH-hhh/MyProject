<template>
    <NavBar />
    <div class="job-banner">
        {{ job.name }}
        <span class="wage">{{ job.wage }}</span>
        <div class="job-intro">
            <p>{{ job.address }}</p>
            <p>{{ job.experience }}</p>
            <p>{{ job.academic }}</p>
        </div>

    </div>
    <ContentBase>
        <b>职位描述</b>
        <div>
            主要内容：
            <div>{{ job.content }}</div>
        </div>
        <div>
            需求:
            <div>{{ job.require }}</div>
        </div>
        <div class="line"></div>
        <div>
            联系方式:
            <div>{{ employer.username }}</div>
            <div>{{ employer.email }}</div>
        </div>
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
        let employer = ref({});

        $.ajax({
            url: 'http://127.0.0.1:8000/api/jobs',
            type: 'GET',
            data: {
                jobid: jobid,
            },
            success: response => {
                job.value = response[0];
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/getotherinfo/',
                    data: {
                        username: job.value.employer
                    },
                    success: response => {
                        // console.log(response);
                        employer.value = response;
                    }
                })
            }
        })
        // console.log(job); 
        return {
            job,
            employer,
        }
    }
}
</script>

<style scoped>
.job-banner {
    height: 200px;
    background-color: #39566C;
    font-size: 28px;
    font-weight: 600;
    color: #fff;
    padding-left: 10vw;
    padding-top: 5vh;
}

.wage {
    font-size: 34px;
    font-family: kanzhun-Regular, kanzhun;
    color: #f26d49;
    line-height: 41px;
    height: auto;
    font-weight: 400;
    position: relative;
    top: -2px;
}

.job-intro>p {
    font-size: 14px;
    color: #fff;
    line-height: 20px;
    height: 20px;
    margin-right: 20px;
    display: inline-block;
}

.line {
    height: 2px;
    border-top: solid #ACC0D8 1px;
}
</style>