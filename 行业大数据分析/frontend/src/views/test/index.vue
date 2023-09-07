<template>
    <div>{{ data }}</div>
</template>

<script>
import { test } from '@/api/job.js';

export default {
    data() {
        return {
            data: null,
        }
    },
    mounted() {
        this.getdata();
    },
    methods: {
        getdata() {
            test().then(response => {
                this.data = response.data;
            })
        }
    }
}
</script>
  
<style lang="scss" scoped>
.dashboard {
    &-container {
        margin: 30px;
    }

    &-text {
        font-size: 30px;
        line-height: 46px;
    }
}
</style>
  