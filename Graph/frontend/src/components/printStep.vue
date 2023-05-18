<template>
    <div class="card all-step">
        <div class="card-body">
            迭代详情
            <div v-for="step in steps.steps" class="card" :key="step.id">
                <div class="card-body">
                    {{ step.content }}
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'printStep',
    props: {
        steps: {
            type: Object,
            required: true
        }
    },
}
</script>

<style scoped>
.card {
    margin-bottom: 2px;
}

.all-step {
    height: 600px;
    overflow: auto;
}
</style>