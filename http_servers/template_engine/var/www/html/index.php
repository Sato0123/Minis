<?php
require_once 'Engine.php';

$engine = new MiniEngine();

// テンプレートに渡すデータ
$data = [
    'title'   => 'テンプレートエンジンのテスト',
    'name'    => 'エンジニア',
    'message' => 'PHP学習'
];

// 表示
echo $engine->render('template.tpl', $data);
