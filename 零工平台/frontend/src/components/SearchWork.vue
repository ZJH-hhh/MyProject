<template>
    <div class="search">
        <input type="text" name="searchWork" maxlength="10" size="70" placeholder="搜索职位">
        <button type="button" class="btn btn-primary search-btn" @click="search">搜索</button>
    </div>
    <div class="search-hot">
        <b>热门职位：</b>
        <a href="">Java</a>
        <a href="">Python</a>
        <a href="">测试工程师</a>
        <a href="">运维工程师</a>
        <a href="">数据分析师</a>
        <a href="">项目经理/主管</a>
    </div>
</template>

<script>
// import $ from 'jquery';
import getjobs from '../api/api.js';

export default {
    name: 'SearchWork',
    setup() {
        // let name = 'django';
        // let author = 'zjh';
        const search = () => {
            getjobs();
        }

        return {
            search,
        }
    }
}
</script>

<style scoped>
.search {
    margin-top: 20px;
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
}

.search-btn {
    font-weight: 500px;
    line-height: 28px;
    margin-left: 2px;
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