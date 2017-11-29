insert into customer_entity (entity_type_id, attribute_set_id, website_id, email, group_id, increment_id, store_id, created_at, updated_at, is_active, disable_auto_group_change, warehouse_id) values (1, 0, 2, 'v.ovchinnikov@kdvm.ru', 15, null, 2, str_to_date('2017-10-29 04:30:17', '%Y-%m-%d %T'), str_to_date('2017-10-29 11:38:24', '%Y-%m-%d %T'), 1, 0, 1);
SET @user_id = LAST_INSERT_ID();
SET @user_email = (SELECT email FROM customer_entity WHERE entity_id = @user_id);
insert into newsletter_subscriber (store_id, change_status_at, customer_id, subscriber_email, subscriber_status, subscriber_confirm_code) values (2, null, @user_id, @user_email, 1, 'wxd7qbgjl3hmk8zjjqybjwyck9aebs49');

insert into customer_entity_int (entity_type_id, attribute_id, entity_id, value) values (1, 14, @user_id, 2317);
insert into customer_entity_int (entity_type_id, attribute_id, entity_id, value) values (1, 286, @user_id, 3);
insert into customer_entity_int (entity_type_id, attribute_id, entity_id, value) values (1, 287, @user_id, 1);
insert into customer_entity_int (entity_type_id, attribute_id, entity_id, value) values (1, 295, @user_id, 1);

insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 3, @user_id, 'Томск');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 5, @user_id, 'Владислав');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 7, @user_id, 'Овчинников');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 12, @user_id, '19bb65710a8feb4176641456f217431a:lYCWGgalauLBZJPRB9mzf1fkU3EoJp7R');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 210, @user_id, '0');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 269, @user_id, '79059926192');

insert into customer_entity_text (entity_type_id, attribute_id, entity_id, value) values (1, 243, @user_id, "634015, г Томск, ул Энергетическая, д 6а");
insert into customer_entity_text (entity_type_id, attribute_id, entity_id, value) values (1, 244, @user_id, "701701001");
insert into customer_entity_text (entity_type_id, attribute_id, entity_id, value) values (1, 260, @user_id, "ООО ТомскАгро");
insert into customer_entity_text (entity_type_id, attribute_id, entity_id, value) values (1, 261, @user_id, "7017168396");

-- *****************

insert into customer_entity (entity_type_id, attribute_set_id, website_id, email, group_id, increment_id, store_id, created_at, updated_at, is_active, disable_auto_group_change, warehouse_id) values (1, 0, 2, 'e.morozov@kdvm.ru', 15, null, 2, str_to_date('2017-10-29 04:30:17', '%Y-%m-%d %T'), str_to_date('2017-10-29 11:38:24', '%Y-%m-%d %T'), 1, 0, 1);
SET @user_id = LAST_INSERT_ID();

insert into customer_address_entity (entity_type_id, attribute_set_id, increment_id, parent_id, created_at, updated_at, is_active, warehouse_id) values (2, 0, null, @user_id, str_to_date('2017-10-12 11:28:37', '%Y-%m-%d %T'), str_to_date('2017-10-13 11:05:04', '%Y-%m-%d %T'), 1, 1);
SET @address_id = LAST_INSERT_ID();

insert into customer_entity_int (entity_type_id, attribute_id, entity_id, value) values (1, 14, @user_id, @address_id);
insert into customer_entity_int (entity_type_id, attribute_id, entity_id, value) values (1, 286, @user_id, 3);
insert into customer_entity_int (entity_type_id, attribute_id, entity_id, value) values (1, 287, @user_id, 1);
insert into customer_entity_int (entity_type_id, attribute_id, entity_id, value) values (1, 295, @user_id, 1);

insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 3, @user_id, 'Томск');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 5, @user_id, 'Евгений');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 7, @user_id, 'Морозов');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 12, @user_id, '19bb65710a8feb4176641456f217431a:lYCWGgalauLBZJPRB9mzf1fkU3EoJp7R');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 210, @user_id, '1');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 269, @user_id, '79233403395');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 273, @user_id, 'Безналичные');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 268, @user_id, '05754197-b482-11e7-810f-fc994749e122');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 272, @user_id, '05754198-b482-11e7-810f-fc994749e122');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 274, @user_id, '2017-10-18T17:00:00+00:00');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 275, @user_id, '0001-12-31 17:49:00+00 BC');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 276, @user_id, '0.00');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 277, @user_id, '3a447597-2ff2-11de-9753-00238b172984');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 278, @user_id, 'false');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 279, @user_id, 'Действует');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 283, @user_id, '193aa026-29a9-11e7-80de-84b8025ba41d');

insert into customer_entity_text (entity_type_id, attribute_id, entity_id, value) values (1, 243, @user_id, "634009, Томская обл, Томск г, Совпартшкольный пер, дом № 12");
insert into customer_entity_text (entity_type_id, attribute_id, entity_id, value) values (1, 244, @user_id, "540101001");
insert into customer_entity_text (entity_type_id, attribute_id, entity_id, value) values (1, 260, @user_id, "ЗАО \"МЕГА -Д\"");
insert into customer_entity_text (entity_type_id, attribute_id, entity_id, value) values (1, 261, @user_id, "7021011694");
-- address point
insert into customer_address_entity_int (entity_type_id, attribute_id, entity_id, value) values (2, 29, @address_id, 0);
insert into customer_address_entity_int (entity_type_id, attribute_id, entity_id, value) values (2, 266, @address_id, 0);
insert into customer_address_entity_int (entity_type_id, attribute_id, entity_id, value) values (2, 292, @address_id, 1);

insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 20, @address_id, 'Евгений');
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 22, @address_id, 'Морозов');
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 24, @address_id, 'Мега');
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 27, @address_id, 'RU');
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 31, @address_id, '79233403395');
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 263, @address_id, 'офис 201');
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 265, @address_id, '3fc5342b-affc-11e7-810d-fc994749e122');
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 267, @address_id, '1d895862-0de8-11e7-80ee-fc994749e122');
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 293, @address_id, '56.4711948');
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 294, @address_id, '84.9655631');
-- метод оплаты
insert into customer_address_entity_text (entity_type_id, attribute_id, entity_id, value) values (2, 25, @address_id, "Томск, пер. Совпартшкольный, 12");
insert into customer_address_entity_text (entity_type_id, attribute_id, entity_id, value) values (2, 264, @address_id, "");




