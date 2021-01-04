<template>
  <el-tabs id="t" v-model="activeName" @tab-click="handleClick">
    <el-tab-pane id="first-tab" label="单条信息处理" name="first">
      <div class="app-container">
        <el-card class="box-card">
          <div>
            {{ text }}
          </div>
        </el-card>
        <el-form ref="form" :model="form" label-width="120px" :rules="rule">
          <el-form-item label="书名" prop="book_name">
            <el-input v-model="form.book_name" />
          </el-form-item>
          <el-form-item label="作者" prop="book_author">
            <el-input v-model="form.book_author" />
          </el-form-item>
          <el-form-item label="出版社" prop="book_public_company">
            <el-input v-model="form.book_public_company" />
          </el-form-item>
          <el-form-item label="ISBN" prop="book_ISBN">
            <el-input v-model="form.book_ISBN" />
            <div style="margin-top: 10px">
              示例：978-7-115-47066-9，必须使用 -（英文字符）进行分隔
            </div>
          </el-form-item>
          <el-form-item label="数量" prop="book_num">
            <el-input v-model="form.book_num" />
          </el-form-item>
          <el-form-item label="中图分类号" prop="book_class">
            <el-input v-model="form.book_class" />
            <div style="margin-top: 10px">
              示例：TP，表示自动化技术、计算机科学类
            </div>
          </el-form-item>
          <el-form-item label="图书状态" prop="book_state">
            <el-select v-model="form.book_state" placeholder="请选择">
              <el-option label="编目" value="1" />
              <el-option label="退货" value="0" />
            </el-select>
          </el-form-item>
          <el-form-item label="退货原因">
            <el-input
              v-model="form.class"
              placeholder="若状态为退货请填退货原因"
            />
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">提交</el-button>
            <el-button @click="onCancel">取消</el-button>
          </el-form-item>
        </el-form>
      </div>
    </el-tab-pane>
    <el-tab-pane label="上传Excel" name="second">
      <div class="app-container">
        <upload-excel-component
          :on-success="handleSuccess"
          :before-upload="beforeUpload"
        />
        <el-button id="upload" type="primary" @click="submitExcel"
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
    <!-- <el-tab-pane label="编目结果" name="thrid">
      <div class="app-container">
        <el-table :data="returnData" stripe style="width: 100%">
          <el-table-column prop="Bname" label="书名" width="180">
          </el-table-column>
          <el-table-column prop="Bauthor" label="作者" width="180">
          </el-table-column>
          <el-table-column prop="Bpub" label="出版社" width="180">
          </el-table-column>
          <el-table-column prop="Bnum" label="在馆数量"> </el-table-column>
        </el-table>
      </div>
    </el-tab-pane> -->
  </el-tabs>
</template>

<script>
import UploadExcelComponent from "@/components/UploadExcel/index.vue";
import { singleCata } from "@/api/catalogue/";
import { Cata } from "@/api/catalogue/";
export default {
  components: { UploadExcelComponent },
  data() {
    return {
      activeName: "first",
      text: "请在此输入编目的书籍信息",
      form: {
        book_name: "cd",
        book_author: "cd",
        book_public_company: "cd",
        book_ISBN: "978-7-115-47066-9",
        book_num: "1",
        book_class: "",
        book_state: "",
        book_return_reason: "",
      },
      tableData: [],
      tableHeader: [],
      up_status: true,
      returnData: [],
      rule: {
        book_name: [
          { required: true, message: "请输入书名", trigger: "blur" },
          // { min: 1, max: 50, message: '长度在 1 到 50 个字符', trigger: 'blur' }
        ],
        book_author: [
          { required: true, message: "请输入作者", trigger: "blur" },
        ],
        book_public_company: [
          { required: true, message: "请输入出版社", trigger: "blur" },
        ],
        book_num: [
          { required: true, message: "请输入数量", trigger: "blur" },
          {
            pattern: /^([1-9]+)[0-9]*$/,
            message: "请输入不以0开头的正确数字",
          },
        ],
        book_ISBN: [
          { required: true, message: "请输入ISBN ", trigger: "blur" },
          {
            pattern: /^((978|979)-)?([0-9]{1,5}-[0-9]{1,6}-[0-9]{1,5}-([0-9]|X))$/,
            message: "ISBN格式有误",
          },
        ],
        book_class: [
          { required: true, message: "请输入中图分类号 ", trigger: "blur" },
          {
            pattern: /^([A-Z]|[a-z])*-?([A-Z]|[0-9])+$/,
            message: "ISBN格式有误",
          },
        ],
        book_state: [{ required: true, trigger: "blur" }],
      },
    };
  },
  methods: {
    //单条编目
    // handleClick(tab, event) {
    //   console.log(tab, event);
    // },
    onSubmit() {
      if (
        this.form.book_name &&
        this.form.book_author &&
        this.form.book_public_company &&
        this.form.book_ISBN &&
        this.form.book_num &&
        this.form.book_class &&
        this.form.book_state
      ) {
        if (this.form.book_state == "0" && !this.form.book_return_reason) {
          this.$message({
            message: "请填写退货原因！",
            type: "warning",
          });
        }
        var formData = new FormData();
        formData.append("book_name", this.form.book_name);
        formData.append("book_author", this.form.book_author);
        formData.append("book_public_company", this.form.book_public_company);
        formData.append("book_ISBN", this.form.book_ISBN);
        formData.append("book_num", this.form.book_num);
        formData.append("book_class", this.form.book_class);
        formData.append("book_state", this.form.book_state);
        formData.append("book_return_reason", this.form.book_return_reason);
        Axios({
          method: "post",
          url: "/api/catalog/addcatalog_one/",
          data: formData,
        }).then(function (res) {
          console.log(res);
          if (res.data.status == 0) {
            _this.$message({
              message: "操作成功！",
              type: "success",
            });
          } else {
            _this.$message({
              message: "出错，请重试",
              type: "error",
            });
          }
        });
      }
    },
    onCancel() {
      this.form = "";
      this.$message({
        message: "取消!",
        type: "warning",
      });
    },

    //excel编目
    beforeUpload(file) {
      const isLt1M = file.size / 1024 / 1024 < 1;
      if (isLt1M) {
        return true;
      } else {
        this.$message({
          message: "Please do not upload files larger than 1m in size.",
          type: "warning",
        });
        return false;
      }
    },
    handleSuccess({ results, header }) {
      let myHeader = [
        "book_name",
        "book_author",
        "book_public_company",
        "book_ISBN",
        "book_class",
        "book_num",
        "book_state",
        "book_return_reason",
      ];
      for (let i = 0; i < myHeader.length; i++) {
        if (header[i] != myHeader[i]) {
          this.$message({
            message: "上传的EXCEL不符合要求",
            type: "warning",
          });
          return;
        }
      }
      if (header.length != myHeader.length) {
        this.$message({
          message: "上传的EXCEL中有多余信息",
          type: "warning",
        });
        return;
      }
      this.tableData = results;
      this.tableHeader = header;
    },
    submitExcel() {
      if (this.tableData && this.tableHeader) {
        this.tableHeader[0]="name";
        console.log(this.tableHeader)
        console.log(this.tableData)
        var data = JSON.stringify(this.tableData);
        console.log(data);
        return ;
        Cata(data).then((res) => {
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
          message: "请先上传文件！",
          type: "warning",
        });
      }
    },
  },
};
</script>

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