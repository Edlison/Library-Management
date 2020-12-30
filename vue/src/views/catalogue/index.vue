<template>
  <el-tabs id="t" v-model="activeName" @tab-click="handleClick">
    <el-tab-pane id="first-tab" label="单条信息编目" name="first">
      <div class="app-container">
        <el-card class="box-card">
          <div>
            {{ text }}
          </div>
        </el-card>
        <el-form ref="form" :model="form" label-width="120px" :rules="rule">
          <el-form-item label="书名" prop="name">
            <el-input v-model="form.name" />
          </el-form-item>
          <el-form-item label="作者" prop="author">
            <el-input v-model="form.author" />
          </el-form-item>
          <el-form-item label="出版社" prop="public">
            <el-input v-model="form.public" />
          </el-form-item>
          <el-form-item label="ISBN" prop="isbn">
            <el-input v-model="form.isbn" />
            <div style="margin-top: 10px">
              示例：978-7-115-47066-9，必须使用 -（英文字符）进行分隔
            </div>
          </el-form-item>
          <el-form-item label="数量" prop="number">
            <el-input v-model="form.number" />
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">提交</el-button>
            <el-button @click="onCancel">取消</el-button>
          </el-form-item>
        </el-form>
      </div>
    </el-tab-pane>
    <el-tab-pane label="上传Excel编目" name="second">
      <div class="app-container">
        <upload-excel-component
          :on-success="handleSuccess"
          :before-upload="beforeUpload"
        />
        <el-button id="upload" type="primary" @click="onSubmit"
          >上传到后台<i class="el-icon-upload el-icon--right"></i
        ></el-button>
        <el-table
          :data="tableData"
          border
          highlight-current-row
          style="width: 100%; margin-top: 20px"
        >
          <el-table-column
            v-for="item of tableHeader"
            :key="item"
            :prop="item"
            :label="item"
          />
        </el-table>
      </div>
    </el-tab-pane>
  </el-tabs>
</template>
<style scoped>
#t {
  margin-left: 10px;
}
.el-select {
  margin-left: 2%;
  margin-bottom: 10px;
}
#upload {
  margin-top: 10px;
  margin-left: 43%;
}
.el-card {
  text-align: center;
  margin: 0 auto 10px auto;
}
.el-select .el-input {
  width: 191px;
}
.input-with-select .el-input-group__prepend {
  background-color: #fff;
}
.text {
  font-size: 14px;
}

.item {
  padding: 18px 0;
}

.box-card {
  width: 480px;
}
</style>
<script>
import UploadExcelComponent from "@/components/UploadExcel/index.vue";
export default {
  components: { UploadExcelComponent },
  data() {
    return {
      activeName: "first",
      text: "请在此输入编目的书籍信息",
      form: {
        name: "",
        author: "",
        public: "",
        class: "",
        isbn: "",
        number: "",
      },
      rule: {
        name: [
          { required: true, message: "请输入书名", trigger: "blur" },
          // { min: 1, max: 50, message: '长度在 1 到 50 个字符', trigger: 'blur' }
        ],
        author: [{ required: true, message: "请输入作者", trigger: "blur" }],
        public: [{ required: true, message: "请输入出版社", trigger: "blur" }],
        number: [
          { required: true, message: "请输入数量", trigger: "blur" },
          {
            pattern: /^([1-9]+)[0-9]*$/, message: "请输入不以0开头的正确数字",
          },
        ],
        isbn: [
          { required: true, message: "请输入ISBN ", trigger: "blur" },
          {
            pattern: /^((978|979)-)?([0-9]{1,5}-[0-9]{1,6}-[0-9]{1,5}-([0-9]|X))$/,
            message: "ISBN格式有误",
          },
        ],
      },
      tableData: [],
      tableHeader: [],
      up_status: true,
    };
  },
  methods: {
    handleClick(tab, event) {
      console.log(tab, event);
    },
    depSubmit() {
      if (this.depForm.name && this.depForm.year) {
        var formData = JSON.stringify(this.depForm);
        console.log(formData);
        upDep(formData).then((res) => {
          if (res.code == 200) {
            this.$message({
              message: "添加成功",
            });
          } else {
            console.log(res);
            this.$message({
              message: "出错，添加失败！",
              type: "warning",
            });
          }
        });
      } else {
        this.$message({
          message: "信息不全！",
          type: "warning",
        });
      }
    },
    onCancel() {
      this.form = "";
      this.$message({
        message: "cancel!",
        type: "warning",
      });
    },
    beforeUpload(file) {
      const isLt1M = file.size / 1024 / 1024 < 1

      if (isLt1M) {
        return true
      }

      this.$message({
        message: 'Please do not upload files larger than 1m in size.',
        type: 'warning'
      })
      return false
    },
    handleSuccess({ results, header }) {
      this.tableData = results
      this.tableHeader = header
    }
  },
};
</script>