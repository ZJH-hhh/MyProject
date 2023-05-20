<template>
    <div class="serach-card">
        <div class="search-box">
            <input v-model="job" type="text" name="searchWork" maxlength="10" size="70" @keydown.enter="search"
                placeholder="搜索职位">
            <button type="button" class="btn btn-primary search-btn" @click="search">搜索</button>
        </div>
        <div class="search-hot">
            <b>热门职位：</b>
            <router-link :to="{ name: 'jobs', params: { 'jobname': 'java' } }">Java</router-link>
            <router-link :to="{ name: 'jobs', params: { 'jobname': 'python' } }">Python</router-link>
            <router-link :to="{ name: 'jobs', params: { 'jobname': '测试工程师' } }">测试工程师</router-link>
            <router-link :to="{ name: 'jobs', params: { 'jobname': '运维工程师' } }">运维工程师</router-link>
            <router-link :to="{ name: 'jobs', params: { 'jobname': '数据分析师' } }">数据分析师</router-link>
            <router-link :to="{ name: 'jobs', params: { 'jobname': '项目经理' } }">项目经理/主管</router-link>
        </div>
    </div>
</template>

<script>
import $ from 'jquery';
// import { getjobs } from '@/api/api';
import { useStore } from 'vuex';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

export default {
    name: 'SearchWork',
    setup() {
        let job = ref('');
        const store = useStore();
        const route = useRouter();

        const search = () => {
            $.ajax({
                url: 'http://127.0.0.1:8000/api/jobs/',
                type: 'GET',
                data: {
                    'jobname': job.value,
                },
                success: response => {
                    console.log(response);
                    route.push({ name: 'jobs', params: { 'jobname': job.value } });
                }
            });
        }

        return {
            job,
            store,
            search,
        }
    }
}
</script>

<style scoped>
.serach-card {
    background-color: #E4F3F5;
}

.search-box {
    /* margin-top: 20px; */
    padding: 20px;
    text-align: center;
}

input {
    height: 50px;
    box-shadow: none;
    font-size: 16px;
    font-weight: 400;
    line-height: 22px;
    padding: 14px 18px;
    border-radius: 12px;
    border: 2px solid #00A6AF;
}

input:focus {
    outline: none;
    /* 移除点击时的默认外边框效果 */
}

.search-btn {
    font-weight: 500px;
    line-height: 28px;
    margin-left: 2px;
    background-color: #00BEBD;
    border: none;
}

.search-hot {
    margin-top: 20px;
    text-align: center;
}

.search-hot>a {
    margin-top: 10px;
    background: rgba(255, 255, 255, .8);
    border-radius: 6px;
    color: #00a6a7;
    font-size: 14px;
    line-height: 20px;
    padding: 2px 8px;
    margin-right: 12px;
    border: 1px solid #00A6AF;
    text-decoration: none;
}

.search-hot>a:hover {
    color: white;
    background-color: #00a6a7;
}
</style>