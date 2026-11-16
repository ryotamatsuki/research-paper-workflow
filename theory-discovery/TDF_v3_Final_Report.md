# Theory Discovery Framework v3.0 最終研究報告

## 完成状況

Theory Discovery Framework（TDF）v3.0を、提案段階ではなく**実際に研究アイデア探索へ使用できる最終実務版**として完成させた。今回の開発では、File Library上で確認できたTDF v1.0の包括報告、10パターン、97件文献DBの存在、SOP、評価ルーブリック、Prompt Library等の成果と、v2.0の4階層・state machine・mechanism fingerprint・反証重視のSOPを継承した。v1.0はすでに「外生変数を内生化する」といったモデル操作よりも、既存理論が何を原因・結果・制度・分析単位として固定しているかを問い直すことが重要だと結論しており、v3.0はこの原理を最終設計の中心に据えた。fileciteturn1file0 fileciteturn1file1

v1.0については、97件の研究文献を収録したDBと30本の中核研究分析が作成されていたことを確認した一方、その過去DBの全レコードや全sandbox成果物を今回の実行環境で再読・再監査できたわけではない。そのため、v3.0では「過去成果を見たことにする」のではなく、確認できた構造を継承しつつ、歴史的に重要な論文をあらためて選び、**10件の継承アンカー＋22件のv3追加調査＝32件**の統合データベースを作成した。v2.0については、四層を固定的な重要度順序ではなく非排他的タグとして用いること、生成・先行研究探索・反証・レビューを明示的に分離する設計を確認し、これもv3.0に残した。fileciteturn1file1 fileciteturn1file2

## 歴史研究から確定したTDFの中核

今回の再調査でも、画期的理論の共通点は「複雑な数式を導入したこと」より、**経済現象のどの部分を所与とみなすかを変更したこと**にあるというv1.0の結論が強く支持された。Coaseは企業を価格理論の所与の主体として扱わず、「価格機構があるのになぜ企業がそもそも生じるのか」を直接問い、企業の存在と境界を説明対象にした。原論文でもfirmがなぜemergeするかを明示的に問題設定している。citeturn999054search8 Grossman–Hartはさらに「所有」を残余コントロール権として捉え直し、不完備契約下の所有権が事後交渉力を介して事前投資を変える理論へ変換した。この視点は後年のレビューでもproperty-rights approachの中心として整理されている。citeturn198828search4turn372340search3

Akerlof型の重要性は「情報の非対称性を入れた」ことだけではない。価格が市場参加者の構成を変え、その構成変化が平均品質と価格を再び変えるという**selection feedback**を市場機構の中心に置いた点にある。原論文は中古車市場を起点としてquality uncertaintyの市場機構を分析している。citeturn999054search1 Spence型では、教育のような行動を直接的生産性だけでなく情報伝達機能として読み替えることで、同じ行動の「第二の経済機能」が理論対象となった。citeturn999054search2 Milgrom–Robertsでは、現在のpredatory actionが後続参入者のbeliefを変えることで将来価値を持つため、行動の意味が現在利得から将来belief stateの操作へ移る。citeturn946494search2

Rochet–Tirole型は、新しい変数を追加するのではなく、既存の「価格」をprice levelとprice structureへ分解したことが本質である。プラットフォームは両側を同時に参加させる必要があるため、同じ総価格でもどちら側に料金を配分するかが参加と取引量を変える。citeturn198828search0turn198828search3 Aghion–Tiroleも権限をformal authorityとreal authorityに分け、法的decision rightと実際の情報優位による支配が一致しないことを理論化した。citeturn971781search2 こうした研究は、TDFにおいて「変数追加」より**既存の十分統計量を分解し、従来同値だった制度を非同値にする**操作を独立パターンとして扱う根拠になった。

もう一つ重要だったのは、理論研究の価値が必ずしも精密な点予測にないことである。Sutton型はゲーム仕様に敏感な点予測よりモデル変更に頑健な市場構造のboundを研究対象にし、Bergemann–Brooks–Morrisは特定の情報構造を固定する代わりに、価格差別下で実現可能な消費者余剰・生産者余剰の集合全体をcharacterizeした。BBMの原論文は、与えられたpriorの下でsegmentationが達成できるwelfare combinationsの範囲を明示的に特徴づけている。citeturn859199search7 この系譜から、TDF v3.0ではRobust Bounds/Invarianceを「特殊なモデル技法」ではなく、独立した発想法として維持した。

産業組織論の歴史全体についても、この設計は整合的である。2014年ノーベル賞のScientific Backgroundは、1970年代末以降のIOをゲーム理論とメカニズムデザインによって大きく変化した「revolution」と位置づけ、従来の一般原則では扱いにくかった個別産業の戦略・情報・規制問題が分析可能になったと整理している。citeturn859199search8 またTirole自身の研究紹介でも、単純な一律政策ではなく、産業固有の情報・戦略構造に合わせて規制を設計する必要性が強調されている。citeturn859199search1turn859199search10

## 発想パターンと実行フローの最終形

v3.0では、v1.0の10パターンを捨てずに、実際の受入テストで反復して必要になった二つを独立化し、**12パターン**とした。追加したのは、P11 Equivalence Breaking（既存理論で同値な制度・政策を隠れた次元により非同値化する）と、P12 Policy-Principle Domain Test（競争促進、情報公開、標準化、補助金等の一般原理が成立する領域と破綻する領域を特定する）である。後者には、Gabaix–Laibsonが競争市場でもshrouded attributesが維持されうることを示した研究が強い歴史的根拠を与える。citeturn971781search7turn971781search0

標準化についても、Katz–Shapiroがnetwork effectsとcompatibilityを企業競争の問題に組み込み、Farrell–Salonerが標準移行をcoordinationとinnovationの問題として分析した既存基盤が強いため、単に「ネットワーク外部性があるから政府標準が必要」という案はTDF上では弱い。citeturn372340search0turn198828search31 v3.0では、標準仕様と更新権限を分解する、標準が「競争の場所」をどの産業層へ移すかを見る、標準化成功が代替技術探索を自己破壊するかを見る、といった**説明構造の変更**がなければ高評価しない。

実行手順は、Phase 1のTheme Map、Phase 2のBaseline Theory Audit、Phase 3のPattern Selection、Phase 4の8–15件程度のcandidate generation、Phase 5のprior-art falsification、Phase 6のvalue screen、Phase 7の研究者とのdialogue loopに統合した。先行研究比較はタイトルや研究対象ではなく、`players / actions / state / information / timing / payoff channel / equilibrium / proposition / policy ranking` からなるmechanism fingerprintで行う。これはv2.0で明確化されていたequivalence検証・fingerprint思想を簡素化して研究者向けに引き継いだものだ。fileciteturn1file1

## 受入テストの主要結果

公的育種では、単純なpublic-good rationaleを超える候補として、**「自治体は完成品種ではなく、将来の気候・病害状態に対応する育種option portfolioを供給している」**という分析単位変更が最も有望だった。公的育種については、民間が十分に投資しにくいminor crops、地域、管理体系、長期的研究やgermplasm等を公的部門が担う根拠が既存研究で指摘されており、したがって単に「民間がやらないから公的に行う」では既存説明に近すぎる。citeturn685977search10turn685977search2 v3.0では、private breeding portfoliosが相関しているほど、低確率・地域固有ショックに備える公的option valueが上がる、という別の理論問いに再構成した。これは未証明の仮説であり、新規性も未確定である。

官民共創拠点では、既存のmatching・spillover・innovation intermediary説明がすでに強い。OECDも研究センターやintermediary organizationsを、企業と研究機関を結び、施設・専門性・共同研究機会を提供する装置として整理している。citeturn685977search4turn685977search5 そのため、最も有望だったのは「拠点はmatching件数を増やす施設ではなく、**relation-specific collaboration optionsを蓄積する市場**」という再定義だった。繰り返しの小規模接触が相手固有情報を作り、それが将来の共同投資optionを価値化する、という動学にすることで、通常のspillover論との差を作れる可能性がある。

標準化政策では、最上位候補は**「技術仕様」と「標準更新権限」の分解**である。同一のcompatibilityを実現する二つの標準でも、改訂、例外承認、認証のresidual control rightsが誰に帰属するかで、補完財企業の事前投資と将来交渉力は変わりうる。これはRochet–Tirole型の概念分解とGrossman–Hart型のproperty-rights reinterpretationを相互作用させた候補であり、単なるnetwork-effectモデルよりTDFの目的に近い。もっともstandard-setting organizationやpatent governanceへの還元可能性は残っており、新規性は`unresolved`である。

地域間産業政策競争では、最も強かった案は**「補助金競争が企業自身のmobility technologyを内生的に変える」**というものだった。通常のtax competitionでは企業の移動可能性を所与とすることが多いが、将来も自治体間で誘致競争が続くと企業がmodular plant、汎用設備、地域非特殊的人的資本等へ投資して自らのoutside optionを高める可能性がある。そうであれば、政策競争は企業を動かすだけでなく「企業をより動きやすい存在に変える」ため、長期的には地域特殊投資とspilloverを弱めるかもしれない。これは現段階では仮説だが、単なる補助率比較とは異なる独立メカニズムになりうる。

未知テーマとしては、前4テーマと異なる現象として**消費者側AI購買エージェントと市場競争**を選んだ。v1.0にAI関連候補が含まれていた可能性があるため完全な初出とは扱っていない。最も有望だったのは、価格を単一の分析単位にせず、final price、machine-readable disclosure、agent access、ranking eligibility等へ分解する案である。Gabaix–Laibson型のshrouding研究が示すように、競争が情報問題を自動的に解消するとは限らないため、AI agentがhuman search costsを下げても、競争がagent-access conditionsやmachine-facing obfuscationへ移る可能性を検討する価値がある。citeturn971781search7

## 納品ファイル

指定された5種類の成果物を、DBのCSV・JSONを分けた**計6ファイル**として作成した。DBには32研究を収録し、各レコードに当時の標準理解、既存理論の限界、着眼点、旧→新の見方、メカニズム、モデル上の工夫、近接先行研究、理論貢献、転用方法、成立条件・限界、パターン、著者動機と再構成の区別、証拠区分、一次資料情報を持たせた。DOIは、今回直接確認できたものを「検証済」、高い確度はあるがこの実行で再照合しなかったものを「高信頼・未再照合」、確認できなかったものを空欄または「DOI未確認」とした。Coase、Akerlof、Spence、Grossman–Hart、Rochet–Tirole、Aghion–Tirole、Armstrong、Gabaix–Laibson、Weyl、BBMなどについては出版社・DOI・一次資料または著者リポジトリで書誌を確認している。citeturn999054search0turn999054search5turn198828search4turn198828search0turn971781search2turn971781search1turn859199search2turn859199search7

- [Economic Theory Discovery Database v3.0 — CSV](sandbox:/mnt/data/tdf_v3/Economic_Theory_Discovery_Database_v3.csv)、[Economic Theory Discovery Database v3.0 — JSON](sandbox:/mnt/data/tdf_v3/Economic_Theory_Discovery_Database_v3.json)、[Theory Discovery Pattern Catalog v3.0](sandbox:/mnt/data/tdf_v3/Theory_Discovery_Pattern_Catalog_v3.md)、[Theory Discovery Framework v3.0](sandbox:/mnt/data/tdf_v3/Theory_Discovery_Framework_v3.md)、[Theory Discovery Master Prompt v3.0](sandbox:/mnt/data/tdf_v3/Theory_Discovery_Master_Prompt_v3.md)、[Theory Discovery User Guide v3.0](sandbox:/mnt/data/tdf_v3/Theory_Discovery_User_Guide_v3.md)

## 限界と未確認事項

v3.0は**実務上利用可能な研究発見フレームワークとして完成**しているが、「この方法を使えば高インパクト理論を高確率で発見できる」という予測性能は検証していない。これはv1.0自身も明示していた制約であり、v2.0のprototypeも有効性を未検証としていた。fileciteturn0file9 fileciteturn1file2 今回の完成条件は、その統計的検証ではなく、歴史的着眼点を再利用可能にし、任意テーマから異なる説明構造を生成し、先行研究との重複を予備的に反証し、研究者との対話によって最小モデルへ進める状態を作ることに置いた。

また、歴史的な「著者が実際にどう思いついたか」は原論文だけでは完全には復元できないため、DBでは本人が明示した動機とTDFによる事後的再構成を区別した。古典文献の一部DOIは今回確証を得られなかったため、推測値を埋めていない。受入テストで示した研究候補も、いずれも**新規性が確立した研究成果ではなく、prior-art falsificationをさらに行うべき研究仮説**である。この慎重な扱いは、TDFの目的を「新規性を宣言する装置」ではなく、「従来と異なる経済的見方を生み、その見方を積極的に壊しながら有望な理論課題を残す知的研究パートナー」に限定するための設計である。