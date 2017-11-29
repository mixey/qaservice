delete from customer_entity_varchar where  entity_id = 1586 and attribute_id = 16;

insert into customer_entity (entity_type_id, attribute_set_id, website_id, email, group_id, increment_id, store_id, created_at, updated_at, is_active, disable_auto_group_change, warehouse_id) values (1, 0, 2, 's.kolesnikov@kdvm.ru', 15, null, 2, str_to_date('2017-10-29 04:30:17', '%Y-%m-%d %T'), str_to_date('2017-10-29 11:38:24', '%Y-%m-%d %T'), 1, 0, 1);
SET @user_id = LAST_INSERT_ID();
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 3, @user_id, 'Томск');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 5, @user_id, 'Колесников');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 7, @user_id, 'Святослав');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 12, @user_id, '19bb65710a8feb4176641456f217431a:lYCWGgalauLBZJPRB9mzf1fkU3EoJp7R');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 16, @user_id, 'f742e77b926c32518daecc1f4c6520d4');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 210, @user_id, '1');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 269, @user_id, '79832343772');


insert into customer_entity (entity_type_id, attribute_set_id, website_id, email, group_id, increment_id, store_id, created_at, updated_at, is_active, disable_auto_group_change, warehouse_id) values (1, 0, 2, 'i.makarov@kdvm.ru', 15, null, 2, str_to_date('2017-10-29 04:30:17', '%Y-%m-%d %T'), str_to_date('2017-10-29 11:38:24', '%Y-%m-%d %T'), 1, 0, 1);
SET @user_id = LAST_INSERT_ID();
SET @user_email = (SELECT email FROM customer_entity WHERE entity_id = @user_id);
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 3, @user_id, 'Томск');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 5, @user_id, 'Макаров');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 7, @user_id, 'Иннокентий');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 12, @user_id, '19bb65710a8feb4176641456f217431a:lYCWGgalauLBZJPRB9mzf1fkU3EoJp7R');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 210, @user_id, '1');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 269, @user_id, '79133433289');
insert into customer_entity_int (entity_type_id, attribute_id, entity_id, value) values (1, 286, @user_id, 1);
insert into customer_entity_int (entity_type_id, attribute_id, entity_id, value) values (1, 287, @user_id, 1);
insert into customer_entity_int (entity_type_id, attribute_id, entity_id, value) values (1, 295, @user_id, 1);
insert into newsletter_subscriber (store_id, change_status_at, customer_id, subscriber_email, subscriber_status, subscriber_confirm_code) values (2, null, @user_id, @user_email, 1, 'wxd7qbgjl3hmk8zjjqybjwyck9aebs49');


insert into customer_entity (entity_type_id, attribute_set_id, website_id, email, group_id, increment_id, store_id, created_at, updated_at, is_active, disable_auto_group_change, warehouse_id) values (1, 0, 2, 'v.kalashnikova@kdvm.ru', 15, null, 2, str_to_date('2017-10-29 04:30:17', '%Y-%m-%d %T'), str_to_date('2017-10-29 11:38:24', '%Y-%m-%d %T'), 1, 0, 1);
SET @user_id = LAST_INSERT_ID();
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 3, @user_id, 'Томск');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 5, @user_id, 'Калашникова');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 7, @user_id, 'Вера');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 12, @user_id, '19bb65710a8feb4176641456f217431a:lYCWGgalauLBZJPRB9mzf1fkU3EoJp7R');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 210, @user_id, '1');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 269, @user_id, '79348538882');


insert into customer_entity (entity_type_id, attribute_set_id, website_id, email, group_id, increment_id, store_id, created_at, updated_at, is_active, disable_auto_group_change, warehouse_id) values (1, 0, 2, 't.bolshakov@kdvm.ru', 15, null, 2, str_to_date('2017-10-29 04:30:17', '%Y-%m-%d %T'), str_to_date('2017-10-29 11:38:24', '%Y-%m-%d %T'), 1, 0, 1);
SET @user_id = LAST_INSERT_ID();
insert into customer_entity_int (entity_type_id, attribute_id, entity_id, value) values (1, 286, @user_id, 1);
insert into customer_entity_int (entity_type_id, attribute_id, entity_id, value) values (1, 287, @user_id, 1);
insert into customer_entity_int (entity_type_id, attribute_id, entity_id, value) values (1, 295, @user_id, 1);

insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 3, @user_id, 'Томск');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 5, @user_id, 'Большаков');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 7, @user_id, 'Тимофей');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 12, @user_id, '19bb65710a8feb4176641456f217431a:lYCWGgalauLBZJPRB9mzf1fkU3EoJp7R');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 210, @user_id, '1');
insert into customer_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (1, 269, @user_id, '79539132324');
-- address 1
insert into customer_address_entity (entity_type_id, attribute_set_id, increment_id, parent_id, created_at, updated_at, is_active, warehouse_id) values (2, 0, null, @user_id, str_to_date('2017-10-23 02:29:17', '%Y-%m-%d %T'), str_to_date('2017-10-23 02:29:17', '%Y-%m-%d %T'), 1, 2);
SET @address_id = LAST_INSERT_ID();
insert into customer_address_entity_int (entity_type_id, attribute_id, entity_id, value) values (2, 29, @address_id, 0);
insert into customer_address_entity_int (entity_type_id, attribute_id, entity_id, value) values (2, 266, @address_id, 0);
insert into customer_address_entity_int (entity_type_id, attribute_id, entity_id, value) values (2, 292, @address_id, 1);
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 20, @address_id, 'Тимофей');
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 22, @address_id, 'Большаков');
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 27, @address_id, 'RU');
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 31, @address_id, '79539132324');
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 293, @address_id, '56.4834717');
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 294, @address_id, '84.9813853');
insert into customer_address_entity_text (entity_type_id, attribute_id, entity_id, value) values (2, 25, @address_id, "Томск, пр. Комсомольский 90, кв. 34");
insert into customer_address_entity_text (entity_type_id, attribute_id, entity_id, value) values (2, 264, @address_id, "");
-- address 2
insert into customer_address_entity (entity_type_id, attribute_set_id, increment_id, parent_id, created_at, updated_at, is_active, warehouse_id) values (2, 0, null, @user_id, str_to_date('2017-10-23 02:29:17', '%Y-%m-%d %T'), str_to_date('2017-10-23 02:29:17', '%Y-%m-%d %T'), 1, 2);
SET @address_id = LAST_INSERT_ID();
insert into customer_address_entity_int (entity_type_id, attribute_id, entity_id, value) values (2, 29, @address_id, 0);
insert into customer_address_entity_int (entity_type_id, attribute_id, entity_id, value) values (2, 266, @address_id, 0);
insert into customer_address_entity_int (entity_type_id, attribute_id, entity_id, value) values (2, 292, @address_id, 1);
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 20, @address_id, 'Денис');
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 22, @address_id, 'Лазарев');
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 27, @address_id, 'RU');
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 31, @address_id, '79223483903');
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 293, @address_id, '56.4834717');
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 294, @address_id, '84.9813853');
insert into customer_address_entity_text (entity_type_id, attribute_id, entity_id, value) values (2, 25, @address_id, "проспект Развития 8, третий этаж, офис 20, Томск");
insert into customer_address_entity_text (entity_type_id, attribute_id, entity_id, value) values (2, 264, @address_id, "");
-- address 3
insert into customer_address_entity (entity_type_id, attribute_set_id, increment_id, parent_id, created_at, updated_at, is_active, warehouse_id) values (2, 0, null, @user_id, str_to_date('2017-10-23 02:29:17', '%Y-%m-%d %T'), str_to_date('2017-10-23 02:29:17', '%Y-%m-%d %T'), 1, 2);
SET @address_id = LAST_INSERT_ID();
insert into customer_address_entity_int (entity_type_id, attribute_id, entity_id, value) values (2, 29, @address_id, 0);
insert into customer_address_entity_int (entity_type_id, attribute_id, entity_id, value) values (2, 266, @address_id, 0);
insert into customer_address_entity_int (entity_type_id, attribute_id, entity_id, value) values (2, 292, @address_id, 1);
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 20, @address_id, 'Григорий');
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 22, @address_id, 'Дроздов');
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 27, @address_id, 'RU');
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 31, @address_id, '79324243434');
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 293, @address_id, '56.4834717');
insert into customer_address_entity_varchar (entity_type_id, attribute_id, entity_id, value) values (2, 294, @address_id, '84.9813853');
insert into customer_address_entity_text (entity_type_id, attribute_id, entity_id, value) values (2, 25, @address_id, "Томск, Лермонтова 32, кв. 2");
insert into customer_address_entity_text (entity_type_id, attribute_id, entity_id, value) values (2, 264, @address_id, "");

