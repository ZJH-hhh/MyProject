<template>
    <NavBar />
    <SearchWork />
    <div class="joblist">
        <ContentBase>
            <div class="card" @click="getjobinfo(job.id)" v-for="job in jobs" :key="job.id">
                <div class="card-body">
                    <div class="job-card-up">
                        <div class="row">
                            <div class="col-6 job-card-left">
                                <div class="row">
                                    <div>{{ job.name }} [{{ job.address }}]</div>
                                </div>
                                <div class="row">
                                    <div class="col-2">
                                        <span class="job-wage">{{ job.wage }}</span>
                                    </div>
                                    <div class="col-10">
                                        <ul class="tag-list">
                                            <li>{{ job.experience }}</li>
                                            <li>{{ job.academic }}</li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div class="col-6 job-card-right">
                                <img src='data:image/jpeg;base64,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'
                                    class="avatar" alt="">
                                {{ job.employer }}
                            </div>
                        </div>
                    </div>
                    <div class="row job-card-down">
                        <div class="col-6">{{ job.tag }}</div>
                        <div class="col-6 job-content">{{ job.content }}</div>
                    </div>
                </div>
            </div>
        </ContentBase>
    </div>
</template>

<script>
// import { getjobs } from '@/api/api';
import $ from 'jquery';
import NavBar from '@/components/NavBar.vue';
import SearchWork from '@/components/SearchWork.vue';
import ContentBase from '@/components/ContentBase.vue';
import { reactive } from 'vue';
import { useRouter, useRoute } from 'vue-router';

export default {
    name: 'WorkList',
    components: {
        NavBar,
        SearchWork,
        ContentBase,
    },
    setup() {
        const router = useRouter();
        const route = useRoute();
        const jobs = reactive([]);
        const jobname = route.params.jobname;

        $.ajax({
            url: 'http://127.0.0.1:8000/api/jobs',
            type: 'GET',
            data: {
                'jobname': jobname,
            },
            success: response => {
                // console.log(response);
                response.forEach(element => {
                    jobs.unshift(element);
                });
            }
        })

        const getjobinfo = jobid => {
            // console.log(jobid);
            router.push({ name: 'job_detail', params: { jobid: jobid } });
        }

        return {
            jobs,
            getjobinfo
        }
    }
}
</script>

<style scoped>
.joblist {
    background-color: #E4F3F5;
}

.card {
    margin-top: 10px;
    border: none;
}

.avatar {
    width: 54.4px;
    height: 54.4px;
}

.card:hover {
    cursor: pointer;
    box-shadow: 8px 8px 10px #E2E2E3,
        -8px 8px 10px #E2E2E3,
        0 8px 10px #E2E2E3;
    color: #00BEBD;
}

/* .card:hover .job-card-left>.row {
    color: #00BEBD;
} */

.tag-list {
    padding: 0;
}

.job-card-down {
    background-color: #F7FBFB;
    font-size: 13px;
    color: #666;
    padding: 5px 0px;
}

.job-content,
.job-require {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.job-info {
    display: flex;
    align-items: center;
}

.job-wage {
    color: #fe574a;
}

span,
li {
    display: inline;
}

.tag-list li {
    margin: 5px;
    line-height: 18px;
    background: #f8f8f8;
    color: #666;
    font-size: 13px;
    padding: 4px;
    border-radius: 4px;
}
</style>