<template>
  <div class="app-container">
    <el-form ref="form" :model="form" label-width="120px">
      <el-form-item label="书名">
        <el-input v-model="form.name" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">提交</el-button>
        <el-button @click="onCancel">取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { deleteBook } from "@/api/deleteBook";
export default {
  data() {
    return {
      form: {
        name: ''
      }
    }
  },
  methods: {
    onSubmit() {
      console.log(this.form);
      if (this.form.name) {
        var formData = this.form;
        deleteBook(formData).then((res) => {
          if (res == "yes") {
            this.$message({
              message: "删除成功！",
            });
          }else if(res == "err_num"){
            this.$message({
          message: "该书借出未还，不能删除！",
          type: "warning",
        });  
          }
          else if(res == "err_book"){
            this.$message({
          message: "馆藏无此书，无法删除！",
          type: "warning",
        });  
          }
        });
      } else {
        this.$message({
          message: "请输入要删书名！",
          type: "warning",
        });
      }
    },
    onCancel() {
        this.form='';
      this.$message({
        message: "取消!",
        type: "warning",
      });
    },
  },
};
</script>

<style scoped>
.line{
  text-align: center;
}
</style>

