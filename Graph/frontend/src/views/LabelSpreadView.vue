<template>
    <ContentBase>
        <div class="row">
            <div class="col-8">
                <displayPart @iteration="iteration" />
            </div>
            <div class="col-4">
                <printStep :steps="steps" />
            </div>
        </div>
    </ContentBase>
</template>

<script>
import { reactive } from 'vue';
import ContentBase from '../components/ContentBase';
import displayPart from '../components/displayPart.vue';
import printStep from '../components/printStep.vue';

export default {
    name: 'LabelSpread',
    components: {
        ContentBase,
        displayPart,
        printStep,
    },
    setup() {
        const steps = reactive({
            steps: [],
        });

        const iteration = content => {
            steps.steps.unshift({
                id: steps.steps.length,
                content: content,
            });
        }

        return {
            steps,
            iteration,
        }
    }
}
</script>

<style scoped>
.btn1 {
    float: left;
}

.btn2 {
    float: right;
}
</style>