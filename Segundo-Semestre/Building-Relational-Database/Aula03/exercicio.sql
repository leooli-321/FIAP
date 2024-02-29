CREATE TABLE T_RHSTU_MEDICO_CONTATO (
  cd_medico number(10) NOT NULL,
  id_contato number(3) NOT NULL,
  tp_contato varchar2(40) NOT NULL,
  ds_contato varchar2(60) NOT NULL,
  st_contato varchar2(1) NOT NULL
);

ALTER TABLE T_RHSTU_MEDICO_CONTATO 
  ADD CONSTRAINT PK_MEDICO_CONTATO PRIMARY KEY (cd_medico, id_contato),
  ADD CONSTRAINT FK_MEDICO_CONTATO FOREIGN KEY (cd_medico) REFERENCES T_RHSTU_MEDICO (cd_medico);

ALTER TABLE T_RHSTU_MEDICO_CONTATO
    ADD id_medico number(10) NOT NULL,
    ADD CONSTRAINT FK_MEDICO FOREIGN KEY (id_medico) REFERENCES MEDICO(id_medico);

-- Certifique-se de que a coluna tp_contato não contém dados que excedam VARCHAR2(2)
ALTER TABLE T_RHSTU_MEDICO_CONTATO
    MODIFY tp_contato VARCHAR2(2);

INSERT INTO MEDICO (id_medico) VALUES (valor_id_medico);

INSERT INTO T_RHSTU_MEDICO_CONTATO (cd_medico, id_contato, tp_contato, ds_contato, st_contato)
VALUES (valor_cd_medico, valor_id_contato, valor_tp_contato, valor_ds_contato, valor_st_contato);

COMMIT;
