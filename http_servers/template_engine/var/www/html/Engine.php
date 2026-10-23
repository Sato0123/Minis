<?php
class MiniEngine {
    public function render($templateFile, $data) {
        // テンプレートファイルを読み込む
        $content = file_get_contents($templateFile);

        // {{key}} を $data['key'] の内容に置換する
        foreach ($data as $key => $value) {
            $content = str_replace("{{" . $key . "}}", htmlspecialchars($value), $content);
        }

        return $content;
    }
}
