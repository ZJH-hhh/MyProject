<template>
    <ContentBase>
        <div class="row">
            <div class="col-4">
                <WorkKind @updateLabel="updateLabel" />
            </div>
            <div class="col-8 same-type">
                <AllWorkOfSameType :jobs="jobs" />
            </div>
        </div>
    </ContentBase>
</template>

<script>
import ContentBase from './ContentBase.vue';
import WorkKind from './WorkKind.vue';
import AllWorkOfSameType from './AllWorkOfSameType.vue';
import { reactive } from 'vue';
import $ from 'jquery';

export default {
    name: 'IntroduceWork',
    components: {
        ContentBase,
        WorkKind,
        AllWorkOfSameType,
    },
    setup() {
        const jobs = reactive([]);

        const updateLabel = tag => {
            // console.log("父组件", tag);
            $.ajax({
                url: 'http://127.0.0.1:8000/api/jobs/',
                type: 'GET',
                data: {
                    'kind': tag,
                },
                success: response => {
                    jobs.splice(0, jobs.length);
                    response.forEach(element => {
                        jobs.push(element);
                    });
                }
            })
        }

        return {
            jobs,
            updateLabel,
        }
    }
}
</script>

<style scoped>
.same-type {
    height: 300px;
    overflow: auto;
}
</style>